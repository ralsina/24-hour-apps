# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Oct 23 12:29:54 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 619)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.output = QtGui.QGraphicsView(self.centralwidget)
        self.output.setObjectName("output")
        self.verticalLayout_2.addWidget(self.output)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.player = phonon.Phonon.VideoPlayer(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player.sizePolicy().hasHeightForWidth())
        self.player.setSizePolicy(sizePolicy)
        self.player.setObjectName("player")
        self.gridLayout.addWidget(self.player, 0, 0, 1, 1)
        self.controls = QtGui.QHBoxLayout()
        self.controls.setObjectName("controls")
        self.play = QtGui.QToolButton(self.dockWidgetContents)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/player_play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon)
        self.play.setCheckable(True)
        self.play.setObjectName("play")
        self.controls.addWidget(self.play)
        self.pause = QtGui.QToolButton(self.dockWidgetContents)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/player_stop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause.setIcon(icon1)
        self.pause.setObjectName("pause")
        self.controls.addWidget(self.pause)
        self.volslider = phonon.Phonon.VolumeSlider(self.dockWidgetContents)
        self.volslider.setObjectName("volslider")
        self.controls.addWidget(self.volslider)
        self.seekslider = phonon.Phonon.SeekSlider(self.dockWidgetContents)
        self.seekslider.setObjectName("seekslider")
        self.controls.addWidget(self.seekslider)
        self.gridLayout.addLayout(self.controls, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(self.dockWidgetContents)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.cutFrom = QtGui.QLineEdit(self.dockWidgetContents)
        self.cutFrom.setObjectName("cutFrom")
        self.horizontalLayout_2.addWidget(self.cutFrom)
        self.markFrom = QtGui.QToolButton(self.dockWidgetContents)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/mark.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.markFrom.setIcon(icon2)
        self.markFrom.setObjectName("markFrom")
        self.horizontalLayout_2.addWidget(self.markFrom)
        self.label_4 = QtGui.QLabel(self.dockWidgetContents)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.cutTo = QtGui.QLineEdit(self.dockWidgetContents)
        self.cutTo.setObjectName("cutTo")
        self.horizontalLayout_2.addWidget(self.cutTo)
        self.markTo = QtGui.QToolButton(self.dockWidgetContents)
        self.markTo.setIcon(icon2)
        self.markTo.setObjectName("markTo")
        self.horizontalLayout_2.addWidget(self.markTo)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cut = QtGui.QToolButton(self.dockWidgetContents)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/editcut.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cut.setIcon(icon3)
        self.cut.setObjectName("cut")
        self.horizontalLayout_2.addWidget(self.cut)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget)
        self.dockWidget_2 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(self.dockWidgetContents_2)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.addAsset = QtGui.QToolButton(self.dockWidgetContents_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/fileopen.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addAsset.setIcon(icon4)
        self.addAsset.setObjectName("addAsset")
        self.horizontalLayout_3.addWidget(self.addAsset)
        self.removeAsset = QtGui.QToolButton(self.dockWidgetContents_2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/fileclose.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeAsset.setIcon(icon5)
        self.removeAsset.setObjectName("removeAsset")
        self.horizontalLayout_3.addWidget(self.removeAsset)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.scrollArea = QtGui.QScrollArea(self.dockWidgetContents_2)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 156))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.assetContainer = QtGui.QWidget(self.scrollArea)
        self.assetContainer.setGeometry(QtCore.QRect(0, 0, 578, 152))
        self.assetContainer.setObjectName("assetContainer")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.assetContainer)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.assets = QtGui.QHBoxLayout()
        self.assets.setObjectName("assets")
        self.horizontalLayout_4.addLayout(self.assets)
        self.scrollArea.setWidget(self.assetContainer)
        self.verticalLayout.addWidget(self.scrollArea)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_2)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pause, QtCore.SIGNAL("clicked()"), self.player.stop)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.play.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pause.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Cut From:", None, QtGui.QApplication.UnicodeUTF8))
        self.markFrom.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Cut To:", None, QtGui.QApplication.UnicodeUTF8))
        self.markTo.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.cut.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Assets", None, QtGui.QApplication.UnicodeUTF8))
        self.addAsset.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.removeAsset.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))

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

