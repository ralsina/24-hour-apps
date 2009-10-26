# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filmlabel.ui'
#
# Created: Mon Oct 26 12:42:36 2009
#      by: PyQt4 UI code generator 4.6.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(128, 154)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.thumb = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(128)
        sizePolicy.setVerticalStretch(128)
        sizePolicy.setHeightForWidth(self.thumb.sizePolicy().hasHeightForWidth())
        self.thumb.setSizePolicy(sizePolicy)
        self.thumb.setMinimumSize(QtCore.QSize(128, 80))
        self.thumb.setMaximumSize(QtCore.QSize(128, 96))
        self.thumb.setPixmap(QtGui.QPixmap(":/icons/film.svg"))
        self.thumb.setScaledContents(True)
        self.thumb.setObjectName("thumb")
        self.verticalLayout.addWidget(self.thumb)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.b1 = QtGui.QToolButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/mark.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b1.setIcon(icon)
        self.b1.setCheckable(True)
        self.b1.setObjectName("b1")
        self.horizontalLayout.addWidget(self.b1)
        self.b2 = QtGui.QToolButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/fileclose.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b2.setIcon(icon1)
        self.b2.setObjectName("b2")
        self.horizontalLayout.addWidget(self.b2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.b1.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.b2.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

