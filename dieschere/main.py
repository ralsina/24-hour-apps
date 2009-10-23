#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The user interface for our app"""

import os,sys

# Import Qt modules
from PyQt4 import QtCore,QtGui
from PyQt4.phonon import Phonon

# Import the compiled UI module
from Ui_main import Ui_MainWindow
from Ui_filmlabel import Ui_Form as Ui_FilmLabel

# Create a class for our main window
class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        # This is always the same
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.mediaObject=None

        # Load a video, so I can implement the media controls

        # Enable-disable buttons as needed
        self.timer=QtCore.QTimer()
        self.assets=QtGui.QButtonGroup()
        self.assets.setExclusive(True)
        self.assets.buttonClicked.connect(self.assetClicked)
        self.ui.centralwidget.adjustSize()
        
    def tick(self):
        t=self.mediaObject.currentTime()
        
    def stateChanged(self, state=None):
        if state is None: return
        
        if state == Phonon.StoppedState:
            self.ui.stop.setEnabled(False)
            self.ui.play.setEnabled(True)
            self.ui.play.setChecked(False)
        elif state == Phonon.PlayingState:
            self.ui.stop.setEnabled(True)
            self.ui.play.setEnabled(True)
            self.ui.play.setChecked(True)
        elif state == Phonon.PausedState:
            self.ui.stop.setEnabled(True)
            self.ui.play.setEnabled(True)
            self.ui.play.setChecked(False)
            
        
    def assetClicked(self, asset=None):
        if asset is None: return
        self.mediaSource=Phonon.MediaSource(asset.fname)
        self.ui.player.load(self.mediaSource)
        self.ui.player.seek(0)
        self.ui.play.setChecked(False)
        self.mediaObject=self.ui.player.mediaObject()
        self.mediaObject.stateChanged.connect(self.stateChanged)
        self.mediaObject.setTickInterval(100)
        self.mediaObject.tick.connect(self.tick)
        #self.ui.seekplaceholder.deleteLater()
        self.ui.seekslider.deleteLater()
        self.ui.volslider.deleteLater()
        self.ui.seekslider=Phonon.SeekSlider(self.mediaObject)
        self.ui.volslider=Phonon.VolumeSlider(self.ui.player.audioOutput())
        self.ui.controls.addWidget(self.ui.seekslider)
        self.ui.controls.addWidget(self.ui.volslider)
                
    def on_play_toggled(self, b):
        if b: #play pressed
            self.ui.player.play()
            self.ui.play.setIcon(QtGui.QIcon(':/icons/pause.svg'))
        else: #pause pressed
            self.ui.player.pause()
            self.ui.play.setIcon(QtGui.QIcon(':/icons/player_play.svg'))

    def on_addAsset_triggered(self, b = None):
        if b is None: return
        
        fname=QtGui.QFileDialog.getOpenFileName()
        if fname:
            # Add an asset for this video
            label=FilmLabel(unicode(fname))
            self.ui.assets.addWidget(label)
            self.assets.addButton(label)

class FilmLabel(QtGui.QPushButton):
    def __init__(self, fname):
        QtGui.QPushButton.__init__(self)
        self.ui=Ui_FilmLabel()
        self.ui.setupUi(self)
        self.fname=fname
        self.setFixedSize(128,128)
        self.setCheckable(True)
        
        # TODO: replace the icon with a capture from the video
        self.ui.label.setText(os.path.basename(fname))
        
    def setChecked(self, b):
        # TODO: Figure out why this is not being called
        
        if b:
            self.label.setBackgroundRole(QtGui.QPalette.Highlight)
            self.label.setForegroundRole(QtGui.QPalette.HighlightedText)
        else:
            self.label.setBackgroundRole(QtGui.QPalette.Window)
            self.label.setForegroundRole(QtGui.QPalette.WindowText)
            
        return QtGui.QPushButton.setChecked(b)
        

def main():
    # Again, this is boilerplate, it's going to be the same on 
    # almost every app you write
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('Die Schere')
    window=Main()
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()
    
