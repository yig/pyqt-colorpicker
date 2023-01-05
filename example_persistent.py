from labcolorpicker import ColorPicker, lab2rgb, rgb2lab
from qtpy.QtWidgets import QApplication
import sys

app = QApplication()

my_color_picker = ColorPicker()
# my_color_picker_light = ColorPicker(lightTheme=True)

def currentColorChangedDark( color ):
    print( "currentColorChangedDark():", color )
my_color_picker.currentColorChanged.connect( currentColorChangedDark )

# def currentColorChangedLight( color ):
#     print( "currentColorChangedLight():", color )
# my_color_picker_light.currentColorChanged.connect( currentColorChangedLight )

print("about to pick")

old_color = rgb2lab((255, 255, 255))
picked_color = my_color_picker.getColor(old_color)
print("picked first")
print(picked_color)



picked_color = my_color_picker.getColor(picked_color)
print("picked second")
print(picked_color)

# picked_color = my_color_picker.getColor(old_color)
# print(picked_color)
# 
# picked_color = my_color_picker_light.getColor(old_color)
# print(picked_color)

sys.exit(app.exec())
