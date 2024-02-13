import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QLabel,QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QFont

from Book_shop_admin import *
from Bookshop_sho_user import *

class Push_btns(QPushButton):
    def __init__(self,text):
        super().__init__(text)   

        self.setFixedSize(500,60)
        self.setStyleSheet("background: gold;color:black;border-radius:15px;font-size:15pt;")
        self.setFont(QFont("Stencil",20))

class Label(QLabel):
    def __init__(self):
        super().__init__()   

        self.setFixedSize(500,100)
        self.setStyleSheet("background: lightblue;color:green;border-radius:15px;font-size:50pt;")
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont("Stencil",20))

class Main(QWidget):
    def __init__(self): 
        super().__init__()

        self.show()
        self.setFixedSize(800,600)
        self.setWindowTitle("BOOK SHOP")
        self.setStyleSheet("background: lightblue")

        self.admin = Push_btns("Admin")
        self.user = Push_btns("User")

        self.label = Label()
        self.label.setText("WELCOME")

        self.h_box = QHBoxLayout()

        self.h_box.addWidget(self.label)

        self.v_box = QVBoxLayout()
        
        self.v_box.addLayout(self.h_box)
        self.v_box.addStretch()
        self.v_box.addWidget(self.admin)
        self.v_box.addWidget(self.user)
        self.v_box.addStretch()
        self.v_box.setAlignment(Qt.AlignCenter)
        
        self.setLayout(self.v_box)

        self.admin.clicked.connect(self.admin_panel)
        self.user.clicked.connect(self.user_panel)

    def admin_panel(self):
        self.ad = Window()
        self.close()
    
    def user_panel(self):
        self.us = Main_user()
        self.close()

app = QApplication(sys.argv)
win = Main()
app.exec_()