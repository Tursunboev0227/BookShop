import mysql.connector

class Core:
    
    def __init__(self) -> None:
        self.__dbConection()

    def __dbConection(self):
        try:
            self.conn = mysql.connector.connect(
                host = 'localhost',
                database = 'bookshop',
                user = 'root',
                password = 'root'
            )
        except Exception as err:
            print(1)
            print(err)
        else:
            print('Database connection is successful')

    def create_book(self,book):
        try:
            with self.conn.cursor() as cursor:
                sql = f"""
                    INSERT INTO books (name,author,genre,pages,price,count) 
                    VALUES (
                    "{book ['name']}",
                    "{book['author']}",
                    "{book['genre']}",
                    "{book['page']}",
                    "{book['price']}",
                    "{book['count']}"
                    );
                """
                cursor.execute(sql)
        except Exception as err:
            return err
        else:
            self.conn.commit()
            return 'CREATED'
    
    def get_all_books(self):
        try:
            with self.conn.cursor() as cursor:
                sql = f'''
                    SELECT * FROM books;
                '''
                cursor.execute(sql)
                data = cursor.fetchall()
        except Exception as err:
            return err
        else:
            return data
        
    
    def setBook(self,book):
        IDS = self.getId()
        if book['id'] in IDS:
            try:
                with self.conn.cursor() as cursor:
                    sql = f"""
                    UPDATE books
                    SET name = '{book['name']}',
                    author = '{book['author']}',
                    genre = '{book['genre']}',
                    pages = '{book['page']}',
                    price = '{book['price']}',
                    count = '{book['count']}'
                    WHERE id = {book['id']};
                    """
                    cursor.execute(sql)
            except Exception as err:
                print(err)
                return 'Entere correct info'
            else:
                self.conn.commit()
                return "UPDATED"
        return 'NOT FOUND'



            
    def getId(self):
        try:
            with self.conn.cursor() as cursor:
                sql = f"""
                    SELECT id FROM books;                    
                """
                cursor.execute(sql)
                ids = cursor.fetchall()
        except Exception as err:
            return err
        else:
            return list(map(lambda id: id[0],ids))
        
    def delete_count(self):
        try:
            with self.conn.cursor() as cuscor:
                sql = f"""
                    DELETE FROM books
                    WHERE count = 0
                """
                cuscor.execute(sql)
        except Exception as err:
            return err
        else:
            self.conn.commit()


        
    def delete(self,book):
        IDS = self.getId()

        if book['id'] in IDS:
            try:
                with self.conn.cursor() as curcor:
                    sql = f"""
                        DELETE FROM books
                        WHERE id = {book['id']};
                    """
                    curcor.execute(sql)
            except Exception as err:
                return err
            else:
                self.conn.commit()
                return "DELETED"
        return 'NOT FOUND'
    
    def get_all_books_user(self):
        try:
            with self.conn.cursor() as cursor:
                sql = f'''
                    SELECT id,name,author,genre,pages,price FROM books;
                '''
                cursor.execute(sql)
                data = cursor.fetchall()
        except Exception as err:
            return err
        else:
            return data
        
    def get_price(self,id):
        try:
            with self.conn.cursor() as cursor:
                sql = f'''
                    SELECT price FROM books
                    WHERE id = '{id}'
                '''
                cursor.execute(sql)
                data = cursor.fetchall()
        except Exception as err:
            return err
        else:
            return data
    
    def minus_count(self,id):
        self.count = self.get_count(id)
        try:
            with self.conn.cursor() as cursor:
                sql = f"""
                    UPDATE books
                    SET count  = '{int(self.count) - 1}'
                    WHERE id = '{id}'
                """
                cursor.execute(sql)
        except Exception as err:
            print(err)
        else:
            self.conn.commit()

    def get_count(self,id):
        try:
            with self.conn.cursor() as cursor:
                sql = f'''
                    SELECT count FROM books
                    WHERE id = '{id}'
                '''
                cursor.execute(sql)
                data = cursor.fetchall()
        except Exception as err:
            return err
        else:
            data = str(list(data[0])[0])
            print(data)
            return data
