import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QLabel,QTableWidget,QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from CORE import *
from main_bookshop import *
class Push_btns(QPushButton):
    def __init__(self,text):
        super().__init__(text)   

        self.setFixedSize(250,50)
        self.setStyleSheet("background: gold;color:black;border-radius:15px;font-size:15pt;")
        self.setFont(QFont("Stencil",20) )

class Edit(QLineEdit):
    def __init__(self):
        super().__init__()   

        self.setFixedSize(480,40)
        self.setStyleSheet("background: gold;color:black;border-radius:15px;font-size:15pt;")
        self.setFont(QFont("Stencil",20))

class Label(QLabel):
    def __init__(self):
        super().__init__()   

        self.setFixedSize(480,40)
        self.setStyleSheet("background: gold;color:black;border-radius:15px;font-size:15pt;")
        self.setFont(QFont("Stencil",20))
class Main_user(QWidget):

    def __init__(self):
        super().__init__()
        self.show()
        self.core = Core()
        self.core.delete_count()

        self.setFixedSize(800,600)
        self.setWindowTitle("BOOK SHOP")
        self.setStyleSheet("background: lightblue")

        self.table = QTableWidget()
        self.purchase = Push_btns("PURCHASE")
        self.show_books = Push_btns("SHOW BOOKS")
        self.exit = Push_btns("EXIT")

        self.v_box = QVBoxLayout()

        self.v_box.addStretch()
        self.v_box.addWidget(self.purchase)
        self.v_box.addWidget(self.show_books)
        self.v_box.addWidget(self.exit)
        self.v_box.setAlignment(Qt.AlignCenter)
        self.v_box.addStretch()

        self.setLayout(self.v_box)

        self.exit.clicked.connect(self.back)
        self.show_books.clicked.connect(self.show_book)
        self.purchase.clicked.connect(self.sall)


    def back(self):
        self.close()

    def show_book(self):
        self.lst = List()
        self.close()

    def sall(self):
        self.s = SELL()
        self.close()
class List(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        self.core = Core()
        self.books = self.get_books()

        self.setWindowTitle('LIST OF  BOOKS')
        self.setFixedSize(1000,600)
        self.setStyleSheet("background: lightblue")

        self.v_box = QVBoxLayout()
        self.table = QTableWidget()

        self.menu = Push_btns("MENU")

        self.books = self.get_books()
        self.table.setColumnCount(6)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 150)
        self.table.setColumnWidth(5, 150)

        
        self.table.setHorizontalHeaderLabels(self.books[0].keys())
        self.table.setRowCount(len(self.books))
        
        row = 0
        for i in self.books:
            self.table.setItem(row, 0, QTableWidgetItem(i['id']))
            self.table.setItem(row, 1, QTableWidgetItem(i['name']))
            self.table.setItem(row, 2, QTableWidgetItem(i['author']))
            self.table.setItem(row, 3, QTableWidgetItem(i['genre']))
            self.table.setItem(row, 4, QTableWidgetItem(i['page']))
            self.table.setItem(row, 5, QTableWidgetItem(i['price']))
            row+=1

        
        self.v_box.addWidget(self.table)
        self.v_box.addWidget(self.menu)
        self.v_box.setAlignment(Qt.AlignCenter)

        self.setLayout(self.v_box)

        self.menu.clicked.connect(self.back)

    def get_books(self):
       books = self.core.get_all_books_user()
       books = list(map(lambda book:{
           'id' :str(book[0]),
           'name' : book[1],
           'author' : book[2],
           'genre' : book[3],
           'page' : str(book[4]),
           'price' : str(book[5])},
           books))
       return books
    
    def back(self):
        self.bc = Main_user()
        self.close()

class SELL(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        self.core = Core()
        self.prices = 0

        self.setWindowTitle('LIST OF  BOOKS')
        self.setFixedSize(1000,600)
        self.setStyleSheet("background: lightblue")

        self.v_box = QVBoxLayout()
        self.table = QTableWidget()

        self.menu = Push_btns("MENU")
        self.menu1 = Push_btns("MENU")

        self.label = Label()
        self.id = Edit()
        self.id.setPlaceholderText("Enter id ")
        self.id.setFixedSize(250,50)

        self.label_err = Label()
    
        self.label_err.setStyleSheet("background: lightblue;color:red;border-radius:15px;font-size:15pt;")
        self.label_err.setFont(QFont("Stencil",20))

        self.purchase = Push_btns('PURCHASE')

        self.h_box = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()

        self.h_box.addWidget(self.label)
        self.h_box2.addWidget(self.id)
        self.h_box3.addWidget(self.purchase)
        self.h_box4.addWidget(self.menu1)

        self.v_box.addLayout(self.h_box)
        self.v_box.addWidget(self.label_err)
        self.v_box.addStretch()   
        self.v_box.addLayout(self.h_box2)   
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)
        self.v_box.addStretch() 
        self.v_box.setAlignment(Qt.AlignCenter)

        self.setLayout(self.v_box)

        self.purchase.clicked.connect(self.pur)
        self.menu1.clicked.connect(self.ret_menu)


    def pur(self):
        id = self.id.text()
        if id:
            self.id.clear()
            self.new = self.core.get_price(id)
            try:
                if self.label.text():
                    self.prices = 0
                    self.core.minus_count(int(id))
                    self.core.delete_count()
                    self.label_err.setText("")


                    self.prices += int(self.label.text())
                    self.new = str(list(self.new[0])[0])
                    print(self.new)
                    self.prices+=int(self.new)
                    self.label.setText(f'{self.prices}')
                else:
                    self.core.minus_count(int(id))
                    self.core.delete_count()
                    self.new = str(list(self.new[0])[0])
                    self.label.setText(self.new)
            except Exception as err:
                self.label_err.setText("NOT FOUND")
        else:
            self.id.clear()
            self.label_err.setText("ENTER ALL INFORMATION")
    
    def ret_menu(self):
        self.bc = Main_user()
        self.close()
