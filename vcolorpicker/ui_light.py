# Form implementation generated from reading ui file 'vcolorpicker/ui/ui_light.ui'
#
# Created by: PyQt6 UI code generator 6.2.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ColorPicker(object):
    def setupUi(self, ColorPicker):
        ColorPicker.setObjectName("ColorPicker")
        ColorPicker.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ColorPicker.sizePolicy().hasHeightForWidth())
        ColorPicker.setSizePolicy(sizePolicy)
        ColorPicker.setMinimumSize(QtCore.QSize(400, 300))
        ColorPicker.setMaximumSize(QtCore.QSize(400, 300))
        ColorPicker.setStyleSheet("QWidget{\n"
"    background-color: none;\n"
"}\n"
"\n"
"/*  LINE EDIT */\n"
"QLineEdit{\n"
"    color: #000;\n"
"    background-color: #bbb;\n"
"    border: 2px solid #bbb;\n"
"    border-radius: 5px;\n"
"    selection-color: rgb(16, 16, 16);\n"
"    selection-background-color: rgb(221, 51, 34);\n"
"    font-family: Segoe UI;\n"
"    font-size: 11pt;\n"
"}\n"
"QLineEdit::focus{\n"
"    border-color: #444;\n"
"}\n"
"\n"
"/* PUSH BUTTON */\n"
"QPushButton{\n"
"    border: 2px solid #777;\n"
"    border-radius: 5px;\n"
"    font-family: Segoe UI;\n"
"    font-size: 9pt;\n"
"    font-weight: bold;\n"
"    color: #333;\n"
"    width: 100px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid #777;\n"
"    color: #111;\n"
"    background-color: #777;\n"
"}\n"
"QPushButton:pressed{\n"
"    border: 2px solid #aaa;\n"
"    color: #222;\n"
"    background-color: #aaa;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(ColorPicker)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.drop_shadow_frame = QtWidgets.QFrame(ColorPicker)
        self.drop_shadow_frame.setStyleSheet("QFrame{\n"
"background-color: #eee;\n"
"border-radius: 10px;\n"
"}")
        self.drop_shadow_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.drop_shadow_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.drop_shadow_frame.setObjectName("drop_shadow_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.title_bar = QtWidgets.QFrame(self.drop_shadow_frame)
        self.title_bar.setMinimumSize(QtCore.QSize(0, 32))
        self.title_bar.setStyleSheet("background-color: #bbb;")
        self.title_bar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(16, 0, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.window_title = QtWidgets.QLabel(self.title_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.window_title.sizePolicy().hasHeightForWidth())
        self.window_title.setSizePolicy(sizePolicy)
        self.window_title.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.window_title.setStyleSheet("QLabel{\n"
"    color: #444;\n"
"    font-family: Segoe UI;\n"
"    font-size: 9pt;\n"
"}")
        self.window_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.window_title.setObjectName("window_title")
        self.horizontalLayout_2.addWidget(self.window_title)
        self.exit_btn = QtWidgets.QPushButton(self.title_bar)
        self.exit_btn.setMinimumSize(QtCore.QSize(16, 16))
        self.exit_btn.setMaximumSize(QtCore.QSize(16, 16))
        self.exit_btn.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.exit_btn.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #888;\n"
"    border-radius: 8px\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #444;\n"
"}")
        self.exit_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/exit.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.exit_btn.setIcon(icon)
        self.exit_btn.setIconSize(QtCore.QSize(12, 12))
        self.exit_btn.setObjectName("exit_btn")
        self.horizontalLayout_2.addWidget(self.exit_btn)
        self.verticalLayout_3.addWidget(self.title_bar)
        self.content_bar = QtWidgets.QFrame(self.drop_shadow_frame)
        self.content_bar.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.content_bar.setStyleSheet("border-radius: 4px")
        self.content_bar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.content_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content_bar.setObjectName("content_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content_bar)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.color_view = QtWidgets.QLabel(self.content_bar)
        self.color_view.setMinimumSize(QtCore.QSize(200, 200))
        self.color_view.setMaximumSize(QtCore.QSize(200, 200))
        self.color_view.setStyleSheet("/* ALL CHANGES HERE WILL BE OVERWRITTEN */;\n"
"background-color: qlineargradient(x1:1, x2:0, stop:0 hsl(0%,100%,50%), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")
        self.color_view.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.color_view.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.color_view.setObjectName("color_view")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.color_view)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.black_overlay = QtWidgets.QFrame(self.color_view)
        self.black_overlay.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border-radius: 4px;\n"
"")
        self.black_overlay.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.black_overlay.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.black_overlay.setObjectName("black_overlay")
        self.selector = QtWidgets.QFrame(self.black_overlay)
        self.selector.setGeometry(QtCore.QRect(194, 20, 12, 12))
        self.selector.setMinimumSize(QtCore.QSize(12, 12))
        self.selector.setMaximumSize(QtCore.QSize(12, 12))
        self.selector.setStyleSheet("background-color:none;\n"
"border: 1px solid white;\n"
"border-radius: 5px;")
        self.selector.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.selector.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.selector.setObjectName("selector")
        self.black_ring = QtWidgets.QLabel(self.selector)
        self.black_ring.setGeometry(QtCore.QRect(1, 1, 10, 10))
        self.black_ring.setMinimumSize(QtCore.QSize(10, 10))
        self.black_ring.setMaximumSize(QtCore.QSize(10, 10))
        self.black_ring.setBaseSize(QtCore.QSize(10, 10))
        self.black_ring.setStyleSheet("background-color: none;\n"
"border: 1px solid black;\n"
"border-radius: 5px;")
        self.black_ring.setText("")
        self.black_ring.setObjectName("black_ring")
        self.verticalLayout_2.addWidget(self.black_overlay)
        self.horizontalLayout.addWidget(self.color_view)
        self.frame_2 = QtWidgets.QFrame(self.content_bar)
        self.frame_2.setMinimumSize(QtCore.QSize(40, 0))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.hue_bg = QtWidgets.QLabel(self.frame_2)
        self.hue_bg.setGeometry(QtCore.QRect(10, 0, 20, 200))
        self.hue_bg.setMinimumSize(QtCore.QSize(20, 200))
        self.hue_bg.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"border-radius: 5px;")
        self.hue_bg.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.hue_bg.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.hue_bg.setObjectName("hue_bg")
        self.hue_selector = QtWidgets.QLabel(self.frame_2)
        self.hue_selector.setGeometry(QtCore.QRect(7, 185, 26, 15))
        self.hue_selector.setMinimumSize(QtCore.QSize(26, 0))
        self.hue_selector.setStyleSheet("background-color: #222;\n"
"border-radius: 5px;")
        self.hue_selector.setText("")
        self.hue_selector.setObjectName("hue_selector")
        self.hue = QtWidgets.QLabel(self.frame_2)
        self.hue.setGeometry(QtCore.QRect(7, 0, 26, 200))
        self.hue.setMinimumSize(QtCore.QSize(20, 200))
        self.hue.setStyleSheet("background-color: none;")
        self.hue.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.hue.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.hue.setObjectName("hue")
        self.horizontalLayout.addWidget(self.frame_2)
        self.editfields = QtWidgets.QFrame(self.content_bar)
        self.editfields.setMinimumSize(QtCore.QSize(110, 200))
        self.editfields.setMaximumSize(QtCore.QSize(120, 200))
        self.editfields.setStyleSheet("QLabel{\n"
"    font-family: Segoe UI;\n"
"    font-weight: bold;\n"
"    font-size: 11pt;\n"
"    color: #666;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.editfields.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.editfields.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.editfields.setObjectName("editfields")
        self.formLayout = QtWidgets.QFormLayout(self.editfields)
        self.formLayout.setContentsMargins(15, 10, 15, 1)
        self.formLayout.setSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.color_vis = QtWidgets.QLabel(self.editfields)
        self.color_vis.setMinimumSize(QtCore.QSize(0, 30))
        self.color_vis.setStyleSheet("/* ALL CHANGES HERE WILL BE OVERWRITTEN */;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.color_vis.setText("")
        self.color_vis.setObjectName("color_vis")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.color_vis)
        self.lastcolor_vis = QtWidgets.QLabel(self.editfields)
        self.lastcolor_vis.setMinimumSize(QtCore.QSize(0, 30))
        self.lastcolor_vis.setStyleSheet("/* ALL CHANGES HERE WILL BE OVERWRITTEN */;\n"
"background-color: rgb(0, 0, 0);")
        self.lastcolor_vis.setText("")
        self.lastcolor_vis.setObjectName("lastcolor_vis")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lastcolor_vis)
        self.lbl_red = QtWidgets.QLabel(self.editfields)
        self.lbl_red.setObjectName("lbl_red")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_red)
        self.red = QtWidgets.QLineEdit(self.editfields)
        self.red.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.red.setClearButtonEnabled(False)
        self.red.setObjectName("red")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.red)
        self.lbl_green = QtWidgets.QLabel(self.editfields)
        self.lbl_green.setObjectName("lbl_green")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_green)
        self.green = QtWidgets.QLineEdit(self.editfields)
        self.green.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.green.setObjectName("green")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.green)
        self.lbl_blue = QtWidgets.QLabel(self.editfields)
        self.lbl_blue.setObjectName("lbl_blue")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_blue)
        self.blue = QtWidgets.QLineEdit(self.editfields)
        self.blue.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.blue.setObjectName("blue")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.blue)
        self.hex = QtWidgets.QLineEdit(self.editfields)
        self.hex.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hex.setObjectName("hex")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.hex)
        self.lbl_hex = QtWidgets.QLabel(self.editfields)
        self.lbl_hex.setStyleSheet("font-size: 14pt;")
        self.lbl_hex.setObjectName("lbl_hex")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_hex)
        self.horizontalLayout.addWidget(self.editfields)
        self.verticalLayout_3.addWidget(self.content_bar)
        self.button_bar = QtWidgets.QFrame(self.drop_shadow_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_bar.sizePolicy().hasHeightForWidth())
        self.button_bar.setSizePolicy(sizePolicy)
        self.button_bar.setStyleSheet("QFrame{\n"
"background-color: #ccc;\n"
"padding: 5px\n"
"}\n"
"")
        self.button_bar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.button_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.button_bar.setObjectName("button_bar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.button_bar)
        self.horizontalLayout_3.setContentsMargins(100, 0, 100, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.button_bar)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout_3.addWidget(self.button_bar)
        self.verticalLayout.addWidget(self.drop_shadow_frame)
        self.lbl_red.setBuddy(self.red)
        self.lbl_green.setBuddy(self.green)
        self.lbl_blue.setBuddy(self.blue)
        self.lbl_hex.setBuddy(self.blue)

        self.retranslateUi(ColorPicker)
        QtCore.QMetaObject.connectSlotsByName(ColorPicker)
        ColorPicker.setTabOrder(self.red, self.green)
        ColorPicker.setTabOrder(self.green, self.blue)

    def retranslateUi(self, ColorPicker):
        _translate = QtCore.QCoreApplication.translate
        ColorPicker.setWindowTitle(_translate("ColorPicker", "Form"))
        self.window_title.setText(_translate("ColorPicker", "<strong>COLOR</strong> PICKER"))
        self.lbl_red.setText(_translate("ColorPicker", "R"))
        self.red.setText(_translate("ColorPicker", "255"))
        self.lbl_green.setText(_translate("ColorPicker", "G"))
        self.green.setText(_translate("ColorPicker", "255"))
        self.lbl_blue.setText(_translate("ColorPicker", "B"))
        self.blue.setText(_translate("ColorPicker", "255"))
        self.hex.setText(_translate("ColorPicker", "ffffff"))
        self.lbl_hex.setText(_translate("ColorPicker", "#"))
