import sys
from PyQt4 import QtCore, QtGui
from multiprocessing import Process
from collections import deque
import pyqtgraph as pg
import pyqtgraph.exporters
import numpy as np
import serial, time

import uRadar

se = serial.Serial(port='/dev/ttyUSB0',
                    baudrate=115200,
                    bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    timeout=0.1)

app = QtGui.QApplication(sys.argv)
num = 0
a = 0
d = 0
a1 = 0
d1 = 0
ang = [0 for num in range(185)]#deque()
dist = [0 for num in range(185)]#deque()
ang1 = []
dist1 = []
appendDir=0;
def update():
	global num, a, d, ang, dist, a1, d1, ang1, dist1, appendDir
	#d = 200+num#abs((num%30)*((np.random.normal(1,10))+1))
	#for n in range(181):
	#print "update1"
	se.write("1")
	msg = se.readline()[:-2]#(se.inWaiting())    # read data from meter
	#print msg
	if (msg != ""): 
		pos = msg.find(",")
		if (pos > 0):
		    if (msg[:pos] != "" and msg[pos+1:] != ""):
			if (msg[pos+1] != ""):
			    a = int(msg[:pos])
			    if a <= 180:
				a1 = a 
			    d = float(msg[pos+1:])
			    if d < 300:
				d1 = d

	#timer.singleShot(10,update)

	
	if a1 >= 0:
		num = a1
		if a1 == 180 or a1 == 0:
			#num = 0
			print "***************** NUM ***************"
			#myapp.curve.clear()
			#ang = []; 
			ang1 = [];
			#dist = []; 
			dist1 = [];
			
			if (a1 == 0):
				appendDir = 1;
			else:
				appendDir = 2;
			

		#print "num =", num, "a1 =", a1, "d1 =", d1, "msg =", msg
		#val1=d1*np.sin((np.pi/180)*a1)
		#val2=d1*np.cos((np.pi/180)*a1)
		myapp.distance.setText(str(d1))
		myapp.angle.setText(str(a1))
		dist1.append(36*np.sin((np.pi/180)*a1))#(d)
		ang1.append(36*np.cos((np.pi/180)*a1))#(a)
		myapp.curve1.setData(ang1,dist1)
		if (d1 > 2 and d1 < 50):
		#if (appendDir%2 == 0):
			dist[a1] = (d1*np.sin((np.pi/180)*a1))#(d)
			ang[a1]= (d1*np.cos((np.pi/180)*a1))#(a)
			#else:
			#dist.append(d1*np.sin((np.pi/180)*a1))#(d)
			#ang.append(d1*np.cos((np.pi/180)*a1))#(a)
			#print ang,dist,appendDir
			myapp.curve.setData(ang,dist)
		else:
			dist[a1] = 0
			ang[a1]= 0
			myapp.curve.setData(ang,dist)
		#dist.append(300*np.sin((np.pi/180)*a1))#(d)
		#ang.append(300*np.cos((np.pi/180)*a1))#(a)
		#myapp.outerCurve.setData(ang,dist)
		#fill = pg.FillBetweenItem(myapp.outerCurve, myapp.curve, 'r')#(fillPlot1, fillPlot2, 'r')#(curve, baseLine, 'r')
		#myapp.polarGraph.addItem(fill)

def update2():
	print "update2"
	fill = pg.FillBetweenItem(myapp.curve, myapp.baseLine, 'r')#(fillPlot1, fillPlot2, 'r')#(curve, baseLine, 'r')
	myapp.polarGraph.addItem(fill)

class RadWin(QtGui.QMainWindow, uRadar.Ui_RadarWindow):
	def __init__(self, parent=None):
		super(RadWin, self).__init__(parent)
		self.setupUi(self)

		line = [0 for num in range(11)]

		# Hide axis
		self.polarGraph.hideAxis('bottom')
		self.polarGraph.hideAxis('left')

		# Add polar grid lines
		self.polarGraph.addLine(x=0, pen=1)
		self.polarGraph.addLine(y=0, pen=1)

		# Add tilted lines at different angles
		for num in range(1,5):
		    line[num-1] = pg.InfiniteLine(pos=[0,0], angle=45*num, pen=1)
		    self.polarGraph.addItem(line[num-1])

		for r in range(0, 40, 6):
		    circle = pg.QtGui.QGraphicsEllipseItem(-r, -r, r*2, r*2)
		    circle.setPen(pg.mkPen(1))
		    self.polarGraph.addItem(circle)

		self.curve = pg.ScatterPlotItem()#self.polarGraph.plot()#pg.PlotCurveItem()#
		self.polarGraph.addItem(self.curve)

		self.curve1 = self.polarGraph.plot()#pg.ScatterPlotItem()#pg.PlotCurveItem()#
		self.polarGraph.addItem(self.curve1)

		x = list(range(-40,1,10))
		y = [0 for r in range(len(x))]
		self.baseLine = pg.PlotCurveItem(pen=1)#pg.ScatterPlotItem()#self.polarGraph.plot()
		self.polarGraph.addItem(self.baseLine)
		self.baseLine.setData(x,y)

		fill = pg.FillBetweenItem(self.curve1, self.baseLine, 'r')#(fillPlot1, fillPlot2, 'r')#(curve, baseLine, 'r')
		self.polarGraph.addItem(fill)

		#self.outerCurve = self.polarGraph.plot()#pg.ScatterPlotItem()#pg.PlotCurveItem()#
		#self.polarGraph.addItem(self.outerCurve)

		

		self.timer = pg.QtCore.QTimer()
		self.timer.timeout.connect(update)
		'''
		p1 = Process(target=self.timer.timeout.connect(update))
		p1.start()
		p2 = Process(target=self.timer.timeout.connect(update2))
		p2.start()
		p1.join()
		p2.join()
		'''

	def __del__(self):
		se.close()
		#self.saveall('auto','autosaves')
		print 'BYE BYE'

	def startAcqPlot(self):
		#time.sleep(2)
		self.timer.start(5)

	def stop(self):
		se.write("0")
		self.timer.stop()


myapp = RadWin()
myapp.show()
app.exec_()
