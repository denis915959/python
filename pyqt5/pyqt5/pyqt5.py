import sys
import codecs #для считывания русских символов
import sqlite3
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QFileDialog, QVBoxLayout, QMainWindow, QPushButton, QLineEdit, QWidget, QLabel, QGroupBox, QGridLayout, QMenuBar, QAction, QInputDialog, QMessageBox
from PyQt5.QtGui import QFont


class Mesh:
	def __init__(self, m_mesh, m_artikul):
		self.mesh=m_mesh
		self.articul=m_artikul
