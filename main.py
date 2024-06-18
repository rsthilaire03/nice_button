from playsound import playsound
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		self.setGeometry(200, 200, 300, 300)
		self.setWindowTitle("Joe Pera")
		self.initUI()
		
	def initUI(self):
		self.button = QtWidgets.QPushButton(self)
		self.button.setText("Nice")
		self.button.move(100, 100)
		self.button.clicked.connect(self.clicked)
		
	def clicked(self):
		playsound("sound.wav")

def window():
	app = QApplication(sys.argv)
	win = MyWindow()
	win.show()
	sys.exit(app.exec_())

window()