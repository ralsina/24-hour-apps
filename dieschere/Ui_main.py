# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon Oct 26 14:18:12 2009
#      by: PyQt4 UI code generator 4.6.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 508)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 645, 28))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
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
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.output = QtGui.QListWidget(self.dockWidgetContents)
        self.output.setFrameShape(QtGui.QFrame.NoFrame)
        self.output.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.output.setDragEnabled(True)
        self.output.setDragDropOverwriteMode(False)
        self.output.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.output.setAlternatingRowColors(True)
        self.output.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.output.setIconSize(QtCore.QSize(96, 96))
        self.output.setTextElideMode(QtCore.Qt.ElideNone)
        self.output.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.output.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.output.setObjectName("output")
        self.verticalLayout_2.addWidget(self.output)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        self.dockWidget_3 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_4 = QtGui.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.assets = QtGui.QListWidget(self.dockWidgetContents_4)
        self.assets.setFrameShape(QtGui.QFrame.NoFrame)
        self.assets.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.assets.setDragEnabled(True)
        self.assets.setDragDropOverwriteMode(False)
        self.assets.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.assets.setAlternatingRowColors(True)
        self.assets.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.assets.setIconSize(QtCore.QSize(96, 96))
        self.assets.setTextElideMode(QtCore.Qt.ElideNone)
        self.assets.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.assets.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.assets.setObjectName("assets")
        self.verticalLayout.addWidget(self.assets)
        self.dockWidget_3.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_3)
        self.addAsset = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/fileopen.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addAsset.setIcon(icon4)
        self.addAsset.setObjectName("addAsset")
        self.actionRender = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/rebuild.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRender.setIcon(icon5)
        self.actionRender.setObjectName("actionRender")
        self.actionSave_Project = QtGui.QAction(MainWindow)
        self.actionSave_Project.setObjectName("actionSave_Project")
        self.actionOpen_Project = QtGui.QAction(MainWindow)
        self.actionOpen_Project.setObjectName("actionOpen_Project")
        self.actionNew_Project = QtGui.QAction(MainWindow)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSaveProject_As = QtGui.QAction(MainWindow)
        self.actionSaveProject_As.setObjectName("actionSaveProject_As")
        self.actionRemove_Asset = QtGui.QAction(MainWindow)
        self.actionRemove_Asset.setObjectName("actionRemove_Asset")
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addAction(self.actionSaveProject_As)
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.addAsset)
        self.menuFile.addAction(self.actionRemove_Asset)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.addAsset)
        self.toolBar.addAction(self.actionRender)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.play.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.stop.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Cut From:", None, QtGui.QApplication.UnicodeUTF8))
        self.markFrom.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Cut To:", None, QtGui.QApplication.UnicodeUTF8))
        self.markTo.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.cut.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_3.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Assets", None, QtGui.QApplication.UnicodeUTF8))
        self.addAsset.setText(QtGui.QApplication.translate("MainWindow", "Add Asset", None, QtGui.QApplication.UnicodeUTF8))
        self.addAsset.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRender.setText(QtGui.QApplication.translate("MainWindow", "Render", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Project.setText(QtGui.QApplication.translate("MainWindow", "Save Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Project.setText(QtGui.QApplication.translate("MainWindow", "Open Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Project.setText(QtGui.QApplication.translate("MainWindow", "New Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveProject_As.setText(QtGui.QApplication.translate("MainWindow", "Save Project As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_Asset.setText(QtGui.QApplication.translate("MainWindow", "Remove Asset", None, QtGui.QApplication.UnicodeUTF8))

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

