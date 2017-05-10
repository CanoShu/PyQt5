# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QSplitter 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Example(QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self): 
		hbox = QHBoxLayout(self)
		self.setWindowTitle('QSplitter demo')
		topleft = QFrame()
		topleft.setFrameShape(QFrame.StyledPanel)
		bottom = QFrame()
		bottom.setFrameShape(QFrame.StyledPanel)
		splitter1 = QSplitter(Qt.Horizontal)
		textedit = QTextEdit()
		splitter1.addWidget(topleft)
		splitter1.addWidget(textedit)
		splitter1.setSizes([100,200])
		splitter2 = QSplitter(Qt.Vertical)
		splitter2.addWidget(splitter1)
		splitter2.addWidget(bottom)
		hbox.addWidget(splitter2)
		self.setLayout(hbox)
		QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
		self.setGeometry(300, 300, 300, 200) 
	
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Example()
	demo.show()
	sys.exit(app.exec_())
