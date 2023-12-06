class SQL:

    seq = 0

    def create(self, table_name="books", *args, **kwargs):
        print("Creando registro nuevo")
        print(table_name)
        print(args)
        print(kwargs)
        SQL.seq += 1
        return SQL.seq

    def update(self, record_id, table_name="books", *args, **kwargs):
        print(f"Actulizando {table_name} con id: {record_id}")
        print(f"Valores: {args}")
        print(kwargs)

    def list(self, table_name="books"):
        print(f"Lista de {table_name}")

    def retrieve(self, record_id, table_name="books"):
        print(f"Se obtiene {record_id} desde {table_name}")

    def delete(self, record_id, table_name="books"):
        print(f"Se elimino {record_id} desde {table_name}")



class Book(SQL):
        content = ''
        def __init__(self, title, author, description):
            self.title = title
            self.author = author
            self.description = description
            self.id = None           

        def save(self):
            self.id = SQL.seq
            self.create('books', self.title, self.author, self.description)

        def update_book(self, record_id, title, author, description):
            super().update(record_id, 'books', title, author, description)
            self.title = title
            self.author = author
            self.description = description

        def delete(self):
            super().delete(self.id,'books')
            del self
        def list(self):
            self.list
        def get(self):
            self.retrieve
        def __str__(self):
            return f'Title= {self.title}, Author= {self.author}, Description= {self.description}, ID= {self.id}'

#Registrando libro 1
book_1 = Book('titulo1', 'autor1','mucho exito1')
book_1.save()

#registrando libro 2
book_2 = Book('titulo2', 'autor2','mucho exito2')
book_2.save()
#registrando libro 3
book_3 = Book('titulo3', 'autor3','mucho exito3')
book_3.save()

#listando libros para ejemplo
book_list = [book_1, book_2, book_3]
for book in book_list:
    print(f'Title: {book.title}, Author: {book.author}, Description: {book.description}')

#updateando libros
book_1.update_book(0,'titulo9', 'autor9','mucho exito9')

#listando libros
print(book_1)

#eliminando libro 3
book_3.delete()









            
            