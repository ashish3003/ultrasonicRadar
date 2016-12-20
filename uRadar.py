# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uRadar.ui'
#
# Created: Mon Dec 12 00:29:35 2016
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_RadarWindow(object):
    def setupUi(self, RadarWindow):
        RadarWindow.setObjectName(_fromUtf8("RadarWindow"))
        RadarWindow.resize(783, 617)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RadarWindow.sizePolicy().hasHeightForWidth())
        RadarWindow.setSizePolicy(sizePolicy)
        RadarWindow.setStyleSheet(_fromUtf8("background-color: rgb(109, 109, 109);"))
        self.centralwidget = QtGui.QWidget(RadarWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.distance = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.distance.setFont(font)
        self.distance.setText(_fromUtf8(""))
        self.distance.setObjectName(_fromUtf8("distance"))
        self.gridLayout.addWidget(self.distance, 1, 1, 1, 1)
        self.stopButton = QtGui.QPushButton(self.centralwidget)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.gridLayout.addWidget(self.stopButton, 2, 2, 1, 2)
        self.distance_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.distance_3.setFont(font)
        self.distance_3.setObjectName(_fromUtf8("distance_3"))
        self.gridLayout.addWidget(self.distance_3, 1, 2, 1, 1)
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.gridLayout.addWidget(self.startButton, 2, 0, 1, 2)
        self.angle = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.angle.setFont(font)
        self.angle.setText(_fromUtf8(""))
        self.angle.setObjectName(_fromUtf8("angle"))
        self.gridLayout.addWidget(self.angle, 1, 3, 1, 1)
        self.distance_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.distance_2.setFont(font)
        self.distance_2.setObjectName(_fromUtf8("distance_2"))
        self.gridLayout.addWidget(self.distance_2, 1, 0, 1, 1)
        self.polarGraph = PlotWidget(self.centralwidget)
        self.polarGraph.setObjectName(_fromUtf8("polarGraph"))
        self.gridLayout.addWidget(self.polarGraph, 0, 0, 1, 4)
        RadarWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(RadarWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuUltrasonic_Radar = QtGui.QMenu(self.menubar)
        self.menuUltrasonic_Radar.setObjectName(_fromUtf8("menuUltrasonic_Radar"))
        RadarWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(RadarWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        RadarWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuUltrasonic_Radar.menuAction())

        self.retranslateUi(RadarWindow)
        QtCore.QObject.connect(self.startButton, QtCore.SIGNAL(_fromUtf8("clicked()")), RadarWindow.startAcqPlot)
        QtCore.QObject.connect(self.stopButton, QtCore.SIGNAL(_fromUtf8("clicked()")), RadarWindow.stop)
        QtCore.QMetaObject.connectSlotsByName(RadarWindow)

    def retranslateUi(self, RadarWindow):
        RadarWindow.setWindowTitle(_translate("RadarWindow", "MainWindow", None))
        self.stopButton.setText(_translate("RadarWindow", "STOP", None))
        self.distance_3.setText(_translate("RadarWindow", "ANGLE", None))
        self.startButton.setText(_translate("RadarWindow", "Start Acquisition", None))
        self.distance_2.setText(_translate("RadarWindow", "DISTANCE", None))
        self.menuUltrasonic_Radar.setTitle(_translate("RadarWindow", "Ultrasonic Radar", None))

from pyqtgraph import PlotWidget
