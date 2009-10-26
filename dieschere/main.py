#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The user interface for our app"""

import os,sys

# Import Qt modules
from PyQt4 import QtCore,QtGui
from PyQt4.phonon import Phonon

# Import the compiled UI module
from Ui_main import Ui_MainWindow

import subprocess 

class Asset(object):
    "Represents a clip, maybe later some other kind of asset"
    def __init__(self,fname):
        self.fname=unicode(fname)
        
    def createItem(self):
        self.item=QtGui.QListWidgetItem(QtGui.QIcon(videoThumb(self.fname)),
            os.path.basename(self.fname))
        self.item.asset=self
        return self.item

# Create a class for our main window
class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        # This is always the same
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.mediaObject=None

        # Enable-disable buttons as needed
        self.timer=QtCore.QTimer()
        self.assets=QtGui.QButtonGroup()
        self.assets.setExclusive(True)
        #self.assets.buttonClicked.connect(self.assetClicked)
        self.ui.centralwidget.adjustSize()
        self.curClip=None

	self.message=QtGui.QLabel()

	self.progress=QtGui.QProgressBar()
	self.progress.setMaximum(100)
	#self.progress.setPercentageVisible(True)
	self.statusBar().addWidget(self.message,1)
	self.statusBar().addWidget(self.progress,0)
        self.progress.hide()
        
        self.assets=[]

    def tick(self):
        t1=self.mediaObject.currentTime()
        t=t1/1000
        if not self.ui.markFrom.isChecked():
            h=t/3600
            m=(t-h*3600)/60
            s=t-h*3600-m*60
            msec=t1-t*1000
            self.ui.cutFrom.setText('%d:%d:%d.%d'%(h,m,s,msec))
        if not self.ui.markTo.isChecked():
            h=t/3600
            m=(t-h*3600)/60
            s=t-h*3600-m*60
            msec=t1-t*1000
            self.ui.cutTo.setText('%d:%d:%d.%d'%(h,m,s,msec))


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
                  
    def on_assets_itemDoubleClicked(self, item=None):
        if item is None: return
        asset = item.asset
        self.ui.output.addItem(asset.createItem())

    def selectClip(self, fname):
        '''Select which clip the player shows'''
        self.curClip=fname
        self.mediaSource=Phonon.MediaSource(fname)
        self.ui.player.load(self.mediaSource)
        self.ui.player.seek(0)
        self.ui.play.setChecked(False)
        self.mediaObject=self.ui.player.mediaObject()
        self.mediaObject.stateChanged.connect(self.stateChanged)
        self.mediaObject.setTickInterval(25)
        self.mediaObject.tick.connect(self.tick)
        #self.ui.seekplaceholder.deleteLater()
        self.ui.seekslider.deleteLater()
        self.ui.volslider.deleteLater()
        self.ui.seekslider=Phonon.SeekSlider(self.mediaObject)
        self.ui.volslider=Phonon.VolumeSlider(self.ui.player.audioOutput())
        self.ui.controls.addWidget(self.ui.seekslider)
        self.ui.controls.addWidget(self.ui.volslider)

    def on_assets_itemClicked(self, item=None):
        if item is None: return
        asset = item.asset
        self.selectClip(asset.fname)
            
    on_output_itemClicked = on_assets_itemClicked        
            
    def on_cut_clicked(self, b=None):
        if b is not None: return
        if not self.curClip: return
        # Cut the current asset's section as selected.
        fname=QtGui.QFileDialog.getSaveFileName()
        if fname:
            # Do the cutting
            
            # mplayer shifts endpos by ss, so if you want a clip from 5 seconds
            # to 10 seconds, it's -ss 5 -endpos 5
            
            if self.ui.markFrom.isChecked():
                h1,m1,s1=map(float,str(self.ui.cutFrom.text()).split(':'))
                t1=h1*3600+m1*60+s1
            else: 
                t1=0
            
            if self.ui.markTo.isChecked():
                h2,m2,s2=map(float,str(self.ui.cutTo.text()).split(':'))
                t2=h2*3600+m2*60+s2
            else:
                t2=99999999
            
            t2=t2-t1            
            
            cmd='mencoder -ovc copy -oac copy %s -ss %s -endpos %s -o %s'%\
                (self.curClip,t1,t2,fname)
            print 'CMD:',cmd
	    self.proc = QtCore.QProcess(self)
	    self.proc.setProcessChannelMode(QtCore.QProcess.MergedChannels)
	    self.proc.readyRead.connect(self.mencoderProgress)
	    self.proc.finished.connect(self.mencoderDone)
	    self.message.setText('Encoding '+ fname)
	    self.proc.start('/usr/bin/mencoder',['-ovc','copy','-oac','copy',self.curClip,
	    '-ss',str(t1),'-endpos',str(t2),'-o',fname])
            # Add asset of the cutted clip
            self.addAsset(fname)

    def mencoderDone(self):
	self.message.setText('Job finished')
	self.progress.hide()

    def mencoderProgress(self):
	self.progress.show()
	l=str(self.proc.readLine())[2:].strip()
	print l
	if 'Pos:' not in l: return 
	pos=int(l.split('(')[1].split('%')[0])
	self.progress.setValue(pos)
            
    def addAsset(self,fname):
        asset=Asset(fname)
        self.assets.append(asset)
        self.ui.assets.addItem(asset.createItem())
        return
            
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
            self.addAsset(fname)
            
    def on_actionRender_triggered(self,b=None):
        if b is not None: return
        fname=QtGui.QFileDialog.getSaveFileName()
        if fname:
            inputs=[]
            i=0
            while True:
                item=self.ui.output.item(i)
                if item is None: break
                inputs.append(item.asset.fname)
                i+=1
	    self.proc = QtCore.QProcess(self)
	    self.proc.setProcessChannelMode(QtCore.QProcess.MergedChannels)
	    self.proc.readyRead.connect(self.mencoderProgress)
	    self.proc.finished.connect(self.mencoderDone)
	    self.message.setText('Encoding '+ fname)
	    self.proc.start('/usr/bin/mencoder',['-ovc','lavc','-oac','mp3lame']+inputs+
						 ['-o',fname])

class FilmLabel(QtGui.QPushButton):
    def __init__(self, fname):
        QtGui.QPushButton.__init__(self)
        self.ui=Ui_FilmLabel()
        self.ui.setupUi(self)
        self.fname=fname
        self.setFixedSize(128,160)
        self.setCheckable(True)
        self.outputLabel=None
        
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
        
        
    def on_b1_toggled(self, b=None):
        if b is None: return
        if self.outputLabel is None:
            if not b: # This is the outputlabel
                self.hide()
            else:
                self.show()
        else: # This is the assetlabel
            if not b:
                self.outputLabel.hide()
            else:
                self.outputLabel.show()
                
def main():
    # Again, this is boilerplate, it's going to be the same on 
    # almost every app you write
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('Die Schere')
    window=Main()
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())

def videoThumb(video):
    td=os.tempnam()
    os.mkdir(td)
    # TODO: port to QProcess
    os.system("mplayer -frames 1 -vo jpeg:outdir=%s '%s' -ao null"%(td,video))
    tname=os.path.join(td,'00000001.jpg')
    thumb=QtGui.QPixmap(tname).scaled(QtCore.QSize(96,96),QtCore.Qt.KeepAspectRatio)
    os.unlink(tname)
    os.rmdir(td)
    return thumb
    


if __name__ == "__main__":
    main()
    
