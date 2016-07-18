# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RC.ui'
#
# Created: Mon Jul 18 00:51:56 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(480, 320)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.page)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btnQuit = QtGui.QPushButton(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnQuit.sizePolicy().hasHeightForWidth())
        self.btnQuit.setSizePolicy(sizePolicy)
        self.btnQuit.setMinimumSize(QtCore.QSize(0, 75))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btnQuit.setFont(font)
        self.btnQuit.setObjectName(_fromUtf8("btnQuit"))
        self.gridLayout.addWidget(self.btnQuit, 2, 0, 1, 1)
        self.btnManual = QtGui.QPushButton(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnManual.sizePolicy().hasHeightForWidth())
        self.btnManual.setSizePolicy(sizePolicy)
        self.btnManual.setMinimumSize(QtCore.QSize(218, 0))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btnManual.setFont(font)
        self.btnManual.setObjectName(_fromUtf8("btnManual"))
        self.gridLayout.addWidget(self.btnManual, 0, 1, 1, 1)
        self.btnAuto = QtGui.QPushButton(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAuto.sizePolicy().hasHeightForWidth())
        self.btnAuto.setSizePolicy(sizePolicy)
        self.btnAuto.setMinimumSize(QtCore.QSize(218, 150))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btnAuto.setFont(font)
        self.btnAuto.setIconSize(QtCore.QSize(24, 24))
        self.btnAuto.setObjectName(_fromUtf8("btnAuto"))
        self.gridLayout.addWidget(self.btnAuto, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.btnShutdown = QtGui.QPushButton(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnShutdown.sizePolicy().hasHeightForWidth())
        self.btnShutdown.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btnShutdown.setFont(font)
        self.btnShutdown.setObjectName(_fromUtf8("btnShutdown"))
        self.gridLayout.addWidget(self.btnShutdown, 2, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lblVoltage = QtGui.QLabel(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblVoltage.sizePolicy().hasHeightForWidth())
        self.lblVoltage.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lblVoltage.setFont(font)
        self.lblVoltage.setObjectName(_fromUtf8("lblVoltage"))
        self.horizontalLayout_3.addWidget(self.lblVoltage)
        self.lblVoltageDisp = QtGui.QLabel(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblVoltageDisp.sizePolicy().hasHeightForWidth())
        self.lblVoltageDisp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lblVoltageDisp.setFont(font)
        self.lblVoltageDisp.setObjectName(_fromUtf8("lblVoltageDisp"))
        self.horizontalLayout_3.addWidget(self.lblVoltageDisp)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.btnQuit, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnQuit.setText(_translate("MainWindow", "Quit", None))
        self.btnManual.setText(_translate("MainWindow", "Manual", None))
        self.btnAuto.setText(_translate("MainWindow", "Auto", None))
        self.label_2.setText(_translate("MainWindow", "TextLabel", None))
        self.btnShutdown.setText(_translate("MainWindow", "Shutdown", None))
        self.lblVoltage.setText(_translate("MainWindow", "Voltage:", None))
        self.lblVoltageDisp.setText(_translate("MainWindow", "1234.5", None))

