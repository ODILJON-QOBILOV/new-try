class Book:
    def __init__(self, title, author, genre, copies=1):
        self.title = title
        self.author = author
        self.genre = genre
        self.copies = copies

    def get_copy(self):
        self.copies += 1
        print(f"Книга \"{self.title}\" была взята из библиотеки. Теперь доступно {self.copies} копий.")

    def return_copy(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"Книга \"{self.title}\" была возвращена в библиотеку. Теперь доступно {self.copies} копий.")
        else:
            print(f"Ошибка: Книги \"{self.title}\" нет в наличии в библиотеке.")

book1 = Book("Война и мир", "Лев Толстой", "Роман", 3)
book2 = Book("Преступление и наказание", "Федор Достоевский", "Роман", 2)
book3 = Book("1984", "Джордж Оруэлл", "Фантастика", 1)

book1.get_copy()
book1.return_copy()
book1.return_copy()
book1.get_copy()
book1.return_copy()
book1.return_copy()
book2.get_copy()
book3.get_copy()
book3.return_copy()
