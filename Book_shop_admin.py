from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QLabel,QTableWidget,QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from CORE import *
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
        
class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.show()
        self.core = Core()
        self.core.delete_count()

        self.setFixedSize(800,600)
        self.setWindowTitle("BOOK SHOP")
        self.setStyleSheet("background: lightblue")

        self.create_book = Push_btns("Create new book")
        self.list_book = Push_btns("List of books")
        self.update_book = Push_btns("Update books")
        self.delete_book = Push_btns("Delete book ")
        self.exit = Push_btns("EXIT")

        
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.v_box.addStretch()
        self.v_box.addWidget(self.create_book)
        self.v_box.addWidget(self.list_book)
        self.v_box.addWidget(self.update_book)
        self.v_box.addWidget(self.delete_book)
        self.v_box.addWidget(self.exit)
        self.v_box.addStretch()


        self.v_box.setAlignment(Qt.AlignCenter)

        self.setLayout(self.v_box)

        self.create_book.clicked.connect(self.__create)
        self.list_book.clicked.connect(self.__list)
        self.update_book.clicked.connect(self.__update)
        self.delete_book.clicked.connect(self.__delete)
        self.exit.clicked.connect(self.__ex)

    def __create(self):
        self.close()
        self.__cr = Create()

    def __list(self):
        self.close()
        self.__cr = List()

    def __update(self):
        self.close()
        self.__cr = Update()
    
    def __delete(self):
        self.close()
        self.__cr = Delete()

    def __ex(self):
        self.close()
        
class Create(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        self.core = Core()

        self.setWindowTitle('CREATE NEW BOOK')
        self.setFixedSize(800,600)
        self.setStyleSheet("background: lightblue")

        self.name = Edit()
        self.name.setPlaceholderText("Enter name of book")

        self.author = Edit()
        self.author.setPlaceholderText("Enter author of boook")

        self.genre = Edit()
        self.genre.setPlaceholderText("Enter ganre of the book")

        self.page = Edit()
        self.page.setPlaceholderText("Enter page of the book")

        self.price = Edit()
        self.price.setPlaceholderText("Enter price")

        self.count = Edit()
        self.count.setPlaceholderText("Enter count of book")

        self.save = Push_btns("SAVE")
        self.save.setFixedSize(480,40)

        self.menu = Push_btns("MENU")
        self.menu.setFixedSize(480,40)

        self.label = Label()

        self.v_box = QVBoxLayout()

        self.v_box.addStretch()
        self.v_box.addWidget(self.label)
        self.v_box.addStretch()
        self.v_box.addWidget(self.name)
        self.v_box.addWidget(self.author)
        self.v_box.addWidget(self.genre)
        self.v_box.addWidget(self.page)
        self.v_box.addWidget(self.price)
        self.v_box.addWidget(self.count)
        self.v_box.addWidget(self.save)
        self.v_box.addStretch()
        self.v_box.addWidget(self.menu)
        self.v_box.setAlignment(Qt.AlignCenter)

        self.setLayout(self.v_box)

        self.btns = [self.name,self.author,self.genre,self.page,self.price,self.count]

        self.menu.clicked.connect(self.__m)
        self.save.clicked.connect(self.save_book)

    def __m(self):
        self.close()
        self.men = Window()

    def save_book(self):
        name = self.name.text()
        author = self.author.text()
        genre = self.genre.text()
        page = self.page.text()
        price = self.price.text()
        count = self.count.text()
        try:
            if name and author and genre and page and price and count:
                book = { 
                    'name' : name,
                    'author' : author,
                    'genre' : genre,
                    'page' : page,
                    'price' : price,
                    'count' : count
                } 
                message = self.core.create_book(book)
                self.label.setText(message)
                self.label.setStyleSheet("background: gold;color:green;border-radius:15px;font-size:15pt;")
                for i in self.btns:
                    i.clear()
            else:
                self.label.setText("ENTER ALL INFORMATION")
                self.label.setStyleSheet("background: gold;color:red;border-radius:15px;font-size:15pt;")

        except Exception as err:

            self.label.setText("Enter corect  version")
            self.label.setStyleSheet("background: gold;color:green;border-radius:15px;font-size:15pt;")

class Update(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        self.core = Core()

        self.setWindowTitle('UPDATE BOOK')
        self.setFixedSize(800,600)
        self.setStyleSheet("background: lightblue")

        self.id = Edit()
        self.id.setPlaceholderText("ID")

        self.name = Edit()
        self.name.setPlaceholderText("Enter name of the book")

        self.author = Edit()
        self.author.setPlaceholderText("Enter author of boook")

        self.genre = Edit()
        self.genre.setPlaceholderText("Enter ganre of the book")

        self.page = Edit()
        self.page.setPlaceholderText("Enter page of the book")

        self.price = Edit()
        self.price.setPlaceholderText("Enter price")

        self.count = Edit()
        self.count.setPlaceholderText("Enter count of books")


        self.upd = Push_btns("UPDATE")
        self.upd.setFixedSize(480,40)

        self.menu = Push_btns("MENU")
        self.menu.setFixedSize(480,40)

        self.label = Label()


        self.v_box = QVBoxLayout()

        self.v_box.addStretch()
        self.v_box.addWidget(self.label)
        self.v_box.addStretch()
        self.v_box.addWidget(self.id)
        self.v_box.addWidget(self.name)
        self.v_box.addWidget(self.author)
        self.v_box.addWidget(self.genre)
        self.v_box.addWidget(self.page)
        self.v_box.addWidget(self.price)
        self.v_box.addWidget(self.count)
        self.v_box.addWidget(self.upd)
        self.v_box.addStretch()
        self.v_box.addWidget(self.menu)
        self.v_box.setAlignment(Qt.AlignCenter)

        self.setLayout(self.v_box)

        self.btns = [self.id,self.name,self.author,self.genre,self.page,self.price,self.count]

        self.menu.clicked.connect(self.__m)
        self.upd.clicked.connect(self.renew)

    def __m(self):
        self.close()
        self.men = Window()
    
    def renew(self):
        ID = self.id.text()
        name = self.name.text()
        author = self.author.text()
        genre = self.genre.text()
        page = self.page.text()
        price = self.price.text()
        count = self.count.text()

        if ID and name and author and genre and page and price and count :
            for i in self.btns:
                i.clear()
            book = {
                'id' : int(ID),
                'name' : name,
                'author' : author,
                'genre' : genre,
                'page' : page,
                'price': int(price),
                'count': int(count)
            }

            message = self.core.setBook(book)
            print(message)
            self.label.setText(message)
            self.label.setStyleSheet("background: gold;color:green;border-radius:15px;font-size:15pt;")

        else:
            self.label.setText("Enter all information")
            self.label.setStyleSheet("background: gold;color:red;border-radius:15px;font-size:15pt;")

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
        self.menu = Push_btns("MENU")
        self.table = QTableWidget()

        self.table.setColumnCount(7)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 150)
        self.table.setColumnWidth(5, 150)
        self.table.setColumnWidth(6, 150)

        
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
            self.table.setItem(row, 6, QTableWidgetItem(i['count']))
            row+=1

        self.v_box.addWidget(self.table)
        self.v_box.addWidget(self.menu)
        self.v_box.setAlignment(Qt.AlignCenter)

        self.setLayout(self.v_box)
        self.menu.clicked.connect(self.__m)

    def get_books(self):
        books = self.core.get_all_books()
        books = list(map(lambda book:{
            'id' :str(book[0]),
            'name' : book[1],
            'author' : book[2],
            'genre' : book[3],
            'page' : str(book[4]),
            'price' : str(book[5]),
            'count' : str(book[6])},
            books))
        return books
    
    def __m(self):
        self.m = Window()
        self.close()

class Delete(QWidget):
    def __init__(self):
        super().__init__()
        self.show()

        self.core = Core()

        self.setWindowTitle('DELETE BOOK')
        self.setFixedSize(800,600)
        self.setStyleSheet("background: lightblue")

        self.id = Edit()
        self.id.setPlaceholderText("ID")

        self.delete = Push_btns("DELETE")
        self.delete.setFixedSize(480,40)

        self.menu = Push_btns("MENU")
        self.menu.setFixedSize(480,40)

        self.label = Label()
        self.v_box = QVBoxLayout()

        self.v_box.addStretch()
        self.v_box.addWidget(self.label)
        self.v_box.addStretch()
        self.v_box.addWidget(self.id)
        self.v_box.addWidget(self.delete)
        self.v_box.addStretch()
        self.v_box.addWidget(self.menu)

        self.v_box.setAlignment(Qt.AlignCenter)

        self.setLayout(self.v_box)
        self.menu.clicked.connect(self.__m)
        self.delete.clicked.connect(self.remove)

    def __m(self):
        self.close()
        self.men = Window()
    
    def remove(self):
        id = self.id.text()

        if id:
            try:
                self.label.setText('')
                book = {
                    'id' : int(id)
                }

                message = self.core.delete(book)
                self.label.setText(message)
                self.id.setText('')
                self.label.setStyleSheet("background: gold;color:green;border-radius:15px;font-size:15pt;")

            except Exception as err:
                self.label.setText("Enter correct information")
                self.label.setStyleSheet("background: gold;color:red;border-radius:15px;font-size:15pt;")

        else:
            self.label.setText("Enter all information")  
            self.label.setStyleSheet("background: gold;color:red;border-radius:15px;font-size:15pt;")