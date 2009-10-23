# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Oct 23 14:53:09 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(611, 540)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(5000, 5000))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.player = phonon.Phonon.VideoPlayer(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player.sizePolicy().hasHeightForWidth())
        self.player.setSizePolicy(sizePolicy)
        self.player.setObjectName("player")
        self.verticalLayout_3.addWidget(self.player)
        self.controls = QtGui.QHBoxLayout()
        self.controls.setObjectName("controls")
        self.play = QtGui.QToolButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/player_play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon)
        self.play.setCheckable(True)
        self.play.setObjectName("play")
        self.controls.addWidget(self.play)
        self.stop = QtGui.QToolButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/player_stop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop.setIcon(icon1)
        self.stop.setObjectName("stop")
        self.controls.addWidget(self.stop)
        self.volslider = phonon.Phonon.VolumeSlider(self.centralwidget)
        self.volslider.setObjectName("volslider")
        self.controls.addWidget(self.volslider)
        self.seekslider = phonon.Phonon.SeekSlider(self.centralwidget)
        self.seekslider.setObjectName("seekslider")
        self.controls.addWidget(self.seekslider)
        self.verticalLayout_3.addLayout(self.controls)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.cutFrom = QtGui.QLineEdit(self.centralwidget)
        self.cutFrom.setObjectName("cutFrom")
        self.horizontalLayout_2.addWidget(self.cutFrom)
        self.markFrom = QtGui.QToolButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/mark.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.markFrom.setIcon(icon2)
        self.markFrom.setCheckable(True)
        self.markFrom.setObjectName("markFrom")
        self.horizontalLayout_2.addWidget(self.markFrom)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.cutTo = QtGui.QLineEdit(self.centralwidget)
        self.cutTo.setObjectName("cutTo")
        self.horizontalLayout_2.addWidget(self.cutTo)
        self.markTo = QtGui.QToolButton(self.centralwidget)
        self.markTo.setIcon(icon2)
        self.markTo.setCheckable(True)
        self.markTo.setObjectName("markTo")
        self.horizontalLayout_2.addWidget(self.markTo)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cut = QtGui.QToolButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/editcut.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cut.setIcon(icon3)
        self.cut.setObjectName("cut")
        self.horizontalLayout_2.addWidget(self.cut)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 611, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea_2 = QtGui.QScrollArea(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(156, 156))
        self.scrollArea_2.setMaximumSize(QtCore.QSize(156, 16777215))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.outputContainer = QtGui.QWidget(self.scrollArea_2)
        self.outputContainer.setGeometry(QtCore.QRect(0, 0, 152, 179))
        self.outputContainer.setObjectName("outputContainer")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.outputContainer)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.output = QtGui.QVBoxLayout()
        self.output.setObjectName("output")
        self.horizontalLayout_5.addLayout(self.output)
        self.scrollArea_2.setWidget(self.outputContainer)
        self.verticalLayout_4.addWidget(self.scrollArea_2)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.dockWidget_3 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_4 = QtGui.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtGui.QScrollArea(self.dockWidgetContents_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(156, 156))
        self.scrollArea.setMaximumSize(QtCore.QSize(156, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.assetContainer = QtGui.QWidget(self.scrollArea)
        self.assetContainer.setGeometry(QtCore.QRect(0, 0, 152, 179))
        self.assetContainer.setObjectName("assetContainer")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.assetContainer)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.assets = QtGui.QVBoxLayout()
        self.assets.setObjectName("assets")
        self.horizontalLayout_4.addLayout(self.assets)
        self.scrollArea.setWidget(self.assetContainer)
        self.verticalLayout.addWidget(self.scrollArea)
        self.dockWidget_3.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_3)
        self.addAsset = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/fileopen.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addAsset.setIcon(icon4)
        self.addAsset.setObjectName("addAsset")
        self.removeAsset = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/fileclose.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeAsset.setIcon(icon5)
        self.removeAsset.setObjectName("removeAsset")
        self.actionMove_Up = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/up.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMove_Up.setIcon(icon6)
        self.actionMove_Up.setObjectName("actionMove_Up")
        self.actionMove_Down = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMove_Down.setIcon(icon7)
        self.actionMove_Down.setObjectName("actionMove_Down")
        self.toolBar.addAction(self.addAsset)
        self.toolBar.addAction(self.actionMove_Up)
        self.toolBar.addAction(self.actionMove_Down)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.play.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.stop.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Cut From:", None, QtGui.QApplication.UnicodeUTF8))
        self.markFrom.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Cut To:", None, QtGui.QApplication.UnicodeUTF8))
        self.markTo.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.cut.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_3.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Assets", None, QtGui.QApplication.UnicodeUTF8))
        self.addAsset.setText(QtGui.QApplication.translate("MainWindow", "Add Asset", None, QtGui.QApplication.UnicodeUTF8))
        self.removeAsset.setText(QtGui.QApplication.translate("MainWindow", "Remove Asset", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMove_Up.setText(QtGui.QApplication.translate("MainWindow", "Move Up", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMove_Down.setText(QtGui.QApplication.translate("MainWindow", "Move Down", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import phonon
import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

