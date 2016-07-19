import sys
from PyQt4 import QtGui, QtCore
from RCui import Ui_MainWindow
import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import threading
from RCCV_findBall import RCCV
RC = RCCV()
#camera = PiCamera()

class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupSignals()

    def setupSignals(self):

        self.ui.btnShutdown.clicked.connect(self.shutdown)
        self.ui.btnAuto.clicked.connect(self.modeAuto)
        self.ui.btnManual.clicked.connect(self.modeManual)
        self.ui.btnQuit.clicked.connect(self.stop)
        
    def modeAuto(self):
        global mode
        mode = 1
        print("Going full auto")

    def modeManual(self):
        global mode
        mode = 0
        print("Going into manual mode")
        
    def shutdown(self):
        from subprocess import call
        call("sudo shutdown --poweroff now", shell=True)

    def testLoop(self):
        global mode
        mode = 0
        global stop
        stop = 0
        while not stop:
            if mode:
                RC.driveAuto()

    def stop(self):
        global stop
        stop = 1


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Main()
    #window.showFullScreen()
    window.show()
    global mode
    global stop
    mode = 0
    stop = 0
    threading.Thread(target=Main().testLoop).start()
    sys.exit(app.exec_())
