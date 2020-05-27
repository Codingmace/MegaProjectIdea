import sys
import random
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton,
							   QVBoxLayout, QWidget)
from PySide2.QtCore import Slot, Qt

""" Takes care of the buttons and can add this asspect
	Need to modify the setup though """


class MyWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		self.hello = ["Hallo Welt", "你好，世界", "Hei maailma",
			"Hola Mundo", "Привет мир"]

		self.button = QPushButton("Click me!")
		self.text = QLabel("Hello World")
		self.text.setAlignment(Qt.AlignCenter)
		self.button1 = QPushButton("No Click eMe")
		self.text1 = QLabel("Better One")
		self.text1.setAlignment(Qt.AlignRight)

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.text)
		self.layout.addWidget(self.button)
		self.layout.addWidget(self.text1)
		self.layout.addWidget(self.button1)
		self.setLayout(self.layout)


		# Connecting the signal
		self.button.clicked.connect(self.magic)

	@Slot()
	def magic(self):
		self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
	app = QApplication(sys.argv)

	widget = MyWidget()
	widget.resize(800, 600)
	widget.show()

	sys.exit(app.exec_())

