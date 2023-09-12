import sys
import codecs #для считывания русских символов
import sqlite3
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QFileDialog, QVBoxLayout, QMainWindow, QPushButton, QLineEdit, QWidget, QLabel, QGroupBox, QGridLayout, QMenuBar, QAction, QInputDialog, QMessageBox
from PyQt5.QtGui import QFont

class robot_path_node:
	def __init__(self, action1, counter1):
		self.action=action1
		self.counter=counter1

def get_number_of_passed_nodes(path, path_num1, path_num2, mesh_num1, mesh_num2):

