# ------------------------------------- #
#                                       #
# Modern Color Picker by Tom F.         #
# Version 1.4.1                         #
# made with Qt Creator & PyQt5          #
#                                       #
# ------------------------------------- #

import colorsys
from typing import Union

from qtpy.QtCore import (QPoint, Qt, Signal)
from qtpy.QtGui import (QColor, QPixmap, QImage)
from qtpy.QtWidgets import (QApplication, QDialog, QGraphicsDropShadowEffect)

from .ui_dark import Ui_ColorPicker as Ui_Dark
from .ui_dark_alpha import Ui_ColorPicker as Ui_Dark_Alpha
from .ui_light import Ui_ColorPicker as Ui_Light
from .ui_light_alpha import Ui_ColorPicker as Ui_Light_Alpha

from .img import *

import numpy as np
import skimage.color

class ColorPicker(QDialog):
    
    currentColorChanged = Signal(tuple)
    
    def __init__(self, lightTheme: bool = False, useAlpha: bool = False, hideButtons: bool = False):
        """Create a new ColorPicker instance.

        :param lightTheme: If the UI should be light themed.
        :param useAlpha: If the ColorPicker should work with alpha values.
        :param hideButtons: If the ColorPicker should hide the OK/Cancel buttons. This leaves only the close box. This is useful if you are listening to `currentColorChanged()` and don't care about the result of `getColor()`.
        """

        # auto-create QApplication if it doesn't exist yet
        self.app = QApplication.instance()
        if self.app is None: self.app = QApplication([])

        super(ColorPicker, self).__init__()

        self.usingAlpha = useAlpha
        self.usingLightTheme = lightTheme

        # Call UI Builder function
        if useAlpha:
            if lightTheme: self.ui = Ui_Light_Alpha()
            else: self.ui = Ui_Dark_Alpha()
        else:
            if lightTheme: self.ui = Ui_Light()
            else: self.ui = Ui_Dark()
        self.ui.setupUi(self)
        if hideButtons:
            self.ui.buttonBox.hide()
        
        # Make Frameless
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowTitle("Color Picker")

        # Add DropShadow
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)

        # Connect update functions
        self.ui.hue.mouseMoveEvent = self.moveLSelector
        self.ui.red.textEdited.connect(self.rgbChanged)
        self.ui.green.textEdited.connect(self.rgbChanged)
        self.ui.blue.textEdited.connect(self.rgbChanged)
        self.ui.hex.textEdited.connect(self.hexChanged)
        if self.usingAlpha: self.ui.alpha.textEdited.connect(self.alphaChanged)

        # Connect window dragging functions
        self.ui.title_bar.mouseMoveEvent = self.moveWindow
        self.ui.title_bar.mousePressEvent = self.setDragPos
        self.ui.window_title.mouseMoveEvent = self.moveWindow
        self.ui.window_title.mousePressEvent = self.setDragPos

        # Connect selector moving function
        self.ui.black_overlay.mouseMoveEvent = self.moveABSelector
        self.ui.black_overlay.mousePressEvent = self.moveABSelector

        # Connect Ok|Cancel Button Box and X Button
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.exit_btn.clicked.connect(self.reject)

        self.lastcolor = (0, 0, 0)
        self.color = (0, 0, 0)
        self.alpha = 100
        self.updateImages()
        
        # self.show()
    
    def setLastColor( self, color: tuple ):
        """Set the last color.
        
        :param color: The color to show as previous color.
        :return: None
        """
        
        color = tuple( color )
        assert len( color ) in (3,4)
        
        if len( color ) > 3: color = color[:3]
        
        ## Update instance variables
        self.lastcolor = color
        
        ## Update GUI
        self.setGUILastColor()
    
    def setCurrentColor( self, color: tuple, skip = None ):
        """Set the current color.
        
        :param color: The color to show as the current color.
        :param skip: Used internally to skip updating a GUI component that triggered the change.
        :return: None
        """
        
        color = tuple( color )
        assert len( color ) in (3,4)
        
        ## Return early if no change
        if color == self.color or color == ( tuple(self.color) + (self.alpha,) ): return
        
        ## Update instance variables.
        if len( color ) > 3:
            self.color, self.alpha = color[:3], color[3]
        else:
            self.color = color
        
        ## Update GUI
        self.setGUICurrentColor( skip )
        
        ## Emit signal
        self.currentColorChanged.emit( color )
    
    def getColor(self, lc: tuple = None):
        """Open the UI and get a color from the user.

        :param lc: The color to show as previous and default color.
        :return: The selected color.
        """
        
        ## Set the previous color
        if lc is not None:
            self.setLastColor( lc )
            
            ## Set the default alpha
            if len(lc) == 4: self.alpha = lc[3]
        
        ## Set the default color
        self.color = self.lastcolor
        
        ## Update the GUI
        self.setGUICurrentColor()
        
        if self.exec_():
            ## Success.
            ## Update the last color.
            self.setLastColor( self.color )
            ## Return the new color:
            if self.usingAlpha:
                return self.color + (self.alpha,)
            else:
                return self.color
        
        else:
            ## Cancel. Return the previous color.
            if self.usingAlpha: return self.lastcolor + (self.alpha,)
            else: return self.lastcolor

    # Update Functions
    def labChanged(self):
        ## Get color from GUI widgets.
        # This is L in the range [0,100]
        L = 100 - self.ui.hue_selector.y() / 1.85
        # a,b are in the range [0,1]
        A = (self.ui.selector.x() + 6) / 200.0
        B = (194 - self.ui.selector.y()) / 200.0
        # Make them [-128,128]
        A = 128.0 * ( A*2.0 - 1.0 )
        B = 128.0 * ( B*2.0 - 1.0 )
        
        color = L,A,B
        
        if color != self.color:
            self.setCurrentColor( color + (self.alpha,) if self.usingAlpha else color, 'lab' )
    
    def rgbChanged(self):
        r,g,b = self.i(self.ui.red.text()), self.i(self.ui.green.text()), self.i(self.ui.blue.text())
        cr,cg,cb = self.clampRGB((r,g,b))
        self.setRGB((cr,cg,cb))

        if r!=cr or (r==0 and self.ui.red.hasFocus()):
            self.ui.red.selectAll()
        if g!=cg or (g==0 and self.ui.green.hasFocus()):
            self.ui.green.selectAll()
        if b!=cb or (b==0 and self.ui.blue.hasFocus()):
            self.ui.blue.selectAll()
        
        color = rgb2lab((cr,cg,cb))
        
        if color != self.color:
            self.setCurrentColor( color + (self.alpha,) if self.usingAlpha else color, 'rgb' )

    def hexChanged(self):
        hex = self.ui.hex.text()
        try:
            int(hex, 16)
        except ValueError:
            hex = "000000"
            self.ui.hex.setText("")
        
        color = hex2lab(hex)
        
        if color != self.color:
            self.setCurrentColor( color + (self.alpha,) if self.usingAlpha else color, 'hex' )

    def alphaChanged(self):
        alpha = self.i(self.ui.alpha.text())
        oldalpha = alpha
        if alpha < 0: alpha = 0
        if alpha > 100: alpha = 100
        if alpha != oldalpha or alpha == 0:
            self.ui.alpha.setText(str(alpha))
            self.ui.alpha.selectAll()
        
        if alpha != self.alpha and self.usingAlpha:
            self.setCurrentColor( self.color + (alpha,), 'alpha' )

    # Internal setting functions
    def setGUICurrentColor(self, skip = None):
        """Update the current color shown in the GUI.
        
        :return: None
        """
        
        if skip != 'lab': self.setLAB( self.color )
        rgb = lab2rgb( self.color )
        if skip != 'rgb': self.setRGB( rgb )
        if skip != 'hex': self.setHex( rgb2hex( rgb ) )
        self.setRGBSwatch( rgb )
        if skip != 'alpha': self.setAlpha( self.alpha )
    
    def setGUILastColor(self):
        """Update the last color shown in the GUI.
        
        :return: None
        """
        
        r,g,b = lab2rgb( self.lastcolor )
        self.ui.lastcolor_vis.setStyleSheet(f"background-color: rgb({r},{g},{b})")
    
    def setRGBSwatch(self, c):
        r,g,b = c
        self.ui.color_vis.setStyleSheet(f"background-color: rgb({r},{g},{b})")
    
    def setRGB(self, c):
        r,g,b = c
        self.ui.red.setText(str(self.i(r)))
        self.ui.green.setText(str(self.i(g)))
        self.ui.blue.setText(str(self.i(b)))

    def setLAB(self, c):
        L,A,B = c
        
        self.ui.hue_selector.move(7, int((100-L) * 1.85))
        self.ui.selector.move(int((0.5*A/128.0 + 0.5) * 200 - 6), int(194 - ((0.5*B/128.0 + 0.5) * 200)))
        
        # Update the images
        self.updateImages()
    
    def updateImages(self):
        L,A,B = self.color
        # print( "LAB:", L, A, B )
        
        gamutAB = np.zeros((200,200,3))
        ## L is fixed.
        gamutAB[:,:,0] = L
        ## A varies from -128 to 128 along the second axis (columns)
        gamutAB[:,:,1] = np.linspace(-128,128,200)[None,:]
        ## B varies from -128 to 128 along the first axis
        gamutAB[:,:,2] = np.linspace(128,-128,200)[:,None]
        self.ui.color_view.setPixmap( QPixmap( QImageFromNumPyImage( skimage.color.lab2rgb( gamutAB ) ) ) )
        
        ## Columns are +x axis on the image.
        ## Rows are -y axis.
        
        # testImage = 0.*gamutAB
        # testImage[:,:,0] = np.linspace(0,1.0,200)[:,None]
        # self.ui.color_view.setPixmap( QPixmap( QImageFromNumPyImage( testImage ) ) )
        
        gamutL = np.zeros((200,20,3))
        ## AB are fixed.
        gamutL[:,:,1] = A
        gamutL[:,:,2] = B
        ## L varies from 0 to 100 alone the second axis
        gamutL[:,:,0] = np.linspace(100,0,200)[:,None]
        self.ui.hue_bg.setPixmap( QPixmap( QImageFromNumPyImage( skimage.color.lab2rgb( gamutL ) ) ) )
    
    def setHex(self, c):
        self.ui.hex.setText(c)

    def setAlpha(self, a):
        if self.usingAlpha: self.ui.alpha.setText(str(a))

    # Dragging Functions
    def setDragPos(self, event):
        self.dragPos = event.globalPos()

    def moveWindow(self, event):
        # MOVE WINDOW
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def moveABSelector(self, event):
        if event.buttons() == Qt.LeftButton:
            pos = event.pos()
            if pos.x() < 0: pos.setX(0)
            if pos.y() < 0: pos.setY(0)
            if pos.x() > 200: pos.setX(200)
            if pos.y() > 200: pos.setY(200)
            self.ui.selector.move(pos - QPoint(6,6))
            self.labChanged()
    
    def moveLSelector(self, event):
        if event.buttons() == Qt.LeftButton:
            pos = event.pos().y() - 7
            if pos < 0: pos = 0
            if pos > 185: pos = 185
            self.ui.hue_selector.move(QPoint(7, pos))
            self.labChanged()

    # Utility

    # Custom int() function, that converts invalid strings to 0
    def i(self, text):
        try: return int(text)
        except ValueError: return 0

    # clamp function to remove near-zero values
    def clampRGB(self, rgb):
        r, g, b = rgb
        if r<0.0001: r=0
        if g<0.0001: g=0
        if b<0.0001: b=0
        if r>255: r=255
        if g>255: g=255
        if b>255: b=255
        return r, g, b


# Color Utility
def lab2rgb(color: tuple) -> tuple:
    """Convert internal lab color to rgb color.

    :param color: The color tuple.
    :return: The converted rgb tuple color.
    """

    return tuple( skimage.color.lab2rgb( np.asarray( color ).astype(float).reshape(1,1,-1) )[0,0]*255.0 )


def rgb2lab(rgb: tuple) -> tuple:
    """Convert rgb color to internal lab color.

    :param rgb: The tuple of red, green, blue values.
    :return: The converted internal lab tuple color.
    """
    
    return tuple( skimage.color.rgb2lab( np.asarray( rgb ).reshape(1,1,-1)/255.0 )[0,0] )

def hex2rgb(hex: str) -> tuple:
    """Convert hex color to rgb color.

    :param hex: The hexadecimal string ("xxxxxx").
    :return: The converted rgb tuple color.
    """

    if len(hex) < 6: hex += "0"*(6-len(hex))
    elif len(hex) > 6: hex = hex[0:6]
    rgb = tuple(int(hex[i:i+2], 16) for i in (0,2,4))
    return rgb


def rgb2hex(rgb: tuple) -> str:
    """Convert rgb color to hex color.

    :param rgb: The tuple of red, green, blue values.
    :return: The converted hexadecimal color.
    """
    
    r,g,b = rgb
    hex = '%02x%02x%02x' % (round(r), round(g), round(b))
    return hex


def hex2lab(hex: str) -> tuple:
    """Convert hex color to internal lab color.

    :param hex: The hexadecimal string ("xxxxxx").
    :return: The converted internal lab tuple color.
    """

    return rgb2lab(hex2rgb(hex))


def lab2hex(color: tuple) -> str:
    """Convert internal lab color to hex color.

    :param color: The color tuple.
    :return: The converted hexadecimal color.
    """

    return rgb2hex(lab2rgb(color))

def QImageFromNumPyImage( arr ):
    ## Source: https://stackoverflow.com/questions/34232632/convert-python-opencv-image-numpy-array-to-pyqt-qpixmap-image
    assert len( arr.shape ) == 3 # width by height by channels
    assert arr.shape[2] == 3 # 3 channels (RGB)
    # Convert to an 8-bit image in contiguous memory
    arr = np.require( (arr*255).round().clip(0,255), dtype = np.uint8, requirements = 'C' )
    # Get parameters
    height, width, channel = arr.shape
    bytesPerLine = 3 * width
    qImg = QImage( arr.data, width, height, bytesPerLine, QImage.Format_RGB888 )
    return qImg

# toplevel functions

__instance = None
__lightTheme = False
__useAlpha = False


def useAlpha(value=True) -> None:
    """Set if the ColorPicker should display an alpha field.

    :param value: True for alpha field, False for no alpha field. Defaults to True
    :return:
    """
    global __useAlpha
    __useAlpha = value


def useLightTheme(value=True) -> None:
    """Set if the ColorPicker should use the light theme.

    :param value: True for light theme, False for dark theme. Defaults to True
    :return: None
    """

    global __lightTheme
    __lightTheme = value


def getColor(lc: tuple = None) -> tuple:
    """Shows the ColorPicker and returns the picked color.

    :param lc: The color to display as previous color.
    :return: The picked color.
    """

    global __instance

    if __instance is None:
        __instance = ColorPicker(useAlpha=__useAlpha, lightTheme=__lightTheme)

    if __useAlpha != __instance.usingAlpha or __lightTheme != __instance.usingLightTheme:
        del __instance
        __instance = ColorPicker(useAlpha=__useAlpha, lightTheme=__lightTheme)

    return __instance.getColor(lc)

