#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The user interface for our app"""

import os,sys,codecs

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
        self.thumb=videoThumb(self.fname)
    def createItem(self):
        self.item=QtGui.QListWidgetItem(QtGui.QIcon(self.thumb),
            os.path.basename(self.fname))
        self.item.asset=self
        return self.item

try:
    import json
except ImportError:
    import simplejson as json


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
        self.ui.centralwidget.adjustSize()
        self.curClip=None

	self.message=QtGui.QLabel()

	self.progress=QtGui.QProgressBar()
	self.progress.setMaximum(100)
	#self.progress.setPercentageVisible(True)
	self.statusBar().addWidget(self.message,1)
	self.statusBar().addWidget(self.progress,0)
        self.progress.hide()
        
        self.projectName=None
        self.setWindowFilePath('None')
        
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

    def on_actionQuit_triggered(self, b=None):
        if b is not None: return
        
        # TODO: warn about losing changes
        self.close()

    def on_actionNew_Project_triggered(self, b=None):
        if b is not None: return
        
        if self.isWindowModified():
            # Make sure we are not losing data
            r=QtGui.QMessageBox.question(self,"Close Document", 
                "The current project has been modified. Do you want to save your changes or discard them?", 
                QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel
                )
            if r==QtGui.QMessageBox.Cancel:
                return
            elif r==QtGui.QMessageBox.Save:
                self.on_actionSave_Project_triggered()
                
        self.ui.assets.clear()
        self.ui.output.clear()
        self.setWindowModified(False)

    def on_actionOpen_Project_triggered(self, b=None):
        if b is not None: return
        fname=QtGui.QFileDialog.getOpenFileName(self,"Open Project",os.getcwd(),"Project Files (*.schere)")
        if fname:
            self.loadProject(fname)
                
    def loadProject(self,fname):
        self.on_actionNew_Project_triggered()
            
        self.projectName=fname
        self.setWindowFilePath(self.projectName)
        proj=json.loads(codecs.open(fname,'r','utf-8').read())
        for fname in proj['assets']:
            self.addAsset(fname)
        for fname in proj['output']:
            self.addAsset(fname,output=True)
        self.setWindowModified(False)
        
    def on_actionSaveProject_As_triggered(self, b=None):
        if b is not None: return
        fname=QtGui.QFileDialog.getSaveFileName(self,"Save Project",os.getcwd(),"Project Files (*.schere)")
        if fname:
            self.projectName=fname
            self.on_actionSave_Project_triggered()    
        else:
            return
            
    def on_actionSave_Project_triggered(self, b=None):
        if b is not None: return
        if not self.projectName:
            self.on_actionSaveProject_As_triggered()

        # A project is the current state of the program.
        # So far, that means:
        # * List of assets
        # * List of output clips
        
        proj={}
        proj['assets']=[]
        proj['output']=[]
        
        for i in range (self.ui.assets.count()):
            proj['assets'].append(self.ui.assets.item(i).asset.fname)
        for i in range (self.ui.output.count()):
            proj['output'].append(self.ui.output.item(i).asset.fname)
        
        codecs.open(self.projectName,'w+','utf-8').write(json.dumps(proj))
        self.setWindowModified(False)
                  
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
        for i in self.ui.output.selectedItems():
            i.setSelected(False)
            
    def on_output_itemClicked(self, item=None):
        if item is None: return
        asset = item.asset
        self.selectClip(asset.fname)
        for i in self.ui.assets.selectedItems():
            i.setSelected(False)
            
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
            
    def addAsset(self,fname,output=False):
        asset=Asset(fname)
        if asset.thumb is None: #Unrecognized formart
            QtGui.QMessageBox.critical(self,"Error opening %s"%fname, "File format not recognized. It doesn't look like a video to me")
            return
        if output:
            self.ui.output.addItem(asset.createItem())
        else:
            self.ui.assets.addItem(asset.createItem())
            
        self.setWindowModified(True)
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
           
    def on_actionRemove_Asset_triggered(self, b = None):
        if b is None: return
        
        item=self.ui.assets.selectedItems()[0]
        if item:
            self.ui.assets.takeItem(self.ui.assets.row(item))
        self.setWindowModified(True)
           
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

def main():
    # Again, this is boilerplate, it's going to be the same on 
    # almost every app you write
    
    
    app = QtGui.QApplication(sys.argv[:1])
    app.setApplicationName('Die Schere')
    window=Main()
    window.show()
    if len(sys.argv) > 1:
        window.loadProject(sys.argv[1])

    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())

def videoThumb(video):
    td=os.tempnam()
    os.mkdir(td)
    try:
        # TODO: port to QProcess
        os.system("mplayer -frames 1 -vo jpeg:outdir=%s '%s' -ao null"%(td,video))
        tname=os.path.join(td,'00000001.jpg')
        thumb=QtGui.QPixmap(tname).scaled(QtCore.QSize(96,96),QtCore.Qt.KeepAspectRatio)
        os.unlink(tname)
        os.rmdir(td)
    except OSError:
        os.rmdir(td)
        return None
    return thumb
    


if __name__ == "__main__":
    main()
    
