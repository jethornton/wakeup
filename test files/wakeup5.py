#!/usr/bin/env python3

import sys
from datetime import datetime, timedelta
from pytz import timezone

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
	QVBoxLayout, QLabel, QAction, qApp)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QIcon

from astral import Location

class main(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowFlags(Qt.WindowStaysOnTopHint)

		updateTimer = QTimer(self)
		updateTimer.timeout.connect(self.update)
		updateTimer.start(1000)

		self.centralWidget = QWidget()
		self.setCentralWidget(self.centralWidget)
		self.layout = QVBoxLayout(self.centralWidget)

		hideAction = QAction(QIcon.fromTheme('window-close'), 'Hide', self)
		hideAction.setShortcut('Ctrl+H')
		hideAction.setStatusTip('Hide Window')
		hideAction.triggered.connect(self.hideWindow)

		exitAct = QAction(QIcon.fromTheme('application-exit'), 'Exit', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.triggered.connect(qApp.quit)
		exitAct.setStatusTip('Exit application')

		toolbar = self.addToolBar('Hide')
		toolbar.addAction(hideAction)
		self.toolbar = self.addToolBar('Exit')
		self.toolbar.addAction(exitAct)

		self.messageLB = QLabel(self)
		self.messageLB.setText('QLabel')
		self.layout.addWidget(self.messageLB)
		self.messageLB.setStyleSheet("border: 1px solid black;")
		self.messageLB.setAlignment(Qt.AlignCenter)

		self.statusLB = QLabel(self)
		self.statusLB.setText('QLabel')
		self.layout.addWidget(self.statusLB)
		self.statusLB.setStyleSheet("border: 1px solid black;")
		self.statusLB.setAlignment(Qt.AlignCenter)

		self.diffLB = QLabel(self)
		self.diffLB.setText('QLabel')
		self.layout.addWidget(self.diffLB)
		self.diffLB.setStyleSheet("border: 1px solid black;")
		self.diffLB.setAlignment(Qt.AlignCenter)

		self.test = 0

		self.location = Location()
		self.location.name = 'Poplar Bluff'
		self.location.region = 'Missouri'
		self.location.latitude = 36.873543
		self.location.longitude = -90.488055
		self.location.timezone = 'US/Central'
		self.location.elevation = "110"
		self.sunrise = self.location.sun()['sunrise']
		#print(type(self.sunrise))

		self.central = timezone('US/Central')

		self.setGeometry(0, 0, 350, 250)
		self.setWindowTitle('Chicken Alarm')
		self.statusBar()
		self.show()

	def update(self):
		now = datetime.now(timezone('US/Central'))
		self.statusBar().showMessage(f'Past Sunrise Today {now > self.sunrise}')
		#print(f'{now}')
		#nowtz = self.central.localize(now)
		#print(f'{nowtz.txinfo}')
		self.messageLB.setText(now.strftime("%Y-%m-%d %H:%M:%S %z %Z"))
		self.statusLB.setText(f'Sunrise {self.sunrise.strftime("%Y-%m-%d %H:%M:%S %z %Z")}')
		#self.diffLB.setText(f'Time Zone {datetime.now(timezone("US/Central"))}')
		if self.sunrise > now:
			diff = self.sunrise - now
			m, s = divmod(int(diff.total_seconds()), 60)
			h, m = divmod(m, 60)
			self.diffLB.setText(f'Next Sunrise in {h:d}:{m:02d}:{s:02d}')
			if h == 0 and m < 30 and self.isHidden():
				self.show()
		else:
			tomorrow = datetime.today() + timedelta(days=1)
			self.sunrise = self.location.sun(tomorrow)['sunrise']

			#self.diffLB.setText('Sunrise has passed')

	def hideWindow(self):
		#print('QMainWindow is Hidden')
		#self.hidden = datetime.now(timezone('US/Central'))
		self.hide()

		'''
		if self.test == 0:
			self.show()
		elif self.test == 3:
			self.hide()
		'''
		if self.test == 5:
			self.test = 0
		else:
			self.test += 1



app = QApplication(sys.argv)
gui = main()
sys.exit(app.exec_())
