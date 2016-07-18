import sys
from PyQt4 import QtGui, QtCore
from RCui import Ui_MainWindow
#import cv2
import numpy as np
#from picamera.array import PiRGBArray
#from picamera import PiCamera
import time

global camera
#camera = PiCamera()

class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupSignals()

    def setupSignals(self):

        self.ui.btnShutdown.clicked.connect(self.shutdown)
        #self.ui.btnApply.clicked.connect(self.setWorkingImg)
    def shutdown(self):
        from subprocess import call
        call("sudo shutdown --poweroff now", shell=True)
    












if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.showFullScreen()
    sys.exit(app.exec_())
