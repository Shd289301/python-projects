class Library():
    def __init__(self, name, booklist):
        self.name = name
        self.booklist = booklist
        self.lendDict = {}


    def display_book(self):
        print(f"Welcome to {self.name} library")
        for book in self.booklist:
            print(book)


    def add_book(self, book):
        if book not in self.booklist:
            self.booklist.append(book)
            print("Book has been added")
            database1 = input("enter data file with extension")
            database2 = open(database1, 'a')
            database2.write('\n')
            database2.write(book)
            print("database has been updated")
        else:
            print(f"book is already there in {self.name} library")

    def lend_book(self, book, user):
        if book in self.booklist:
            if book not in self.lendDict.keys():
                self.lendDict.update({book: user})
                print(f"{book} book has been lend and updated to database")
            else:
                print(f"{book} book has been borrowed by some other user")
        else:
            print(f"{book} book not available in {self.name} library")

    def return_book(self, book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print(f"{book} book has been returned and database has been updated")
        else:
            print(f"{book} book has not been borrowed")
def main():
    bookList = []
    Name = input("enter library name:")
    datafile = input("enter file name with extension")
    database = open(datafile, 'r')
    for book in database:
        bookList.append(book)
    accept = True
    library = Library(Name, bookList)
    while accept:
        option = input("select C to continue or Q to quit:")
        if option == 'C':
            print("menu details to continue:")
            menu = '''
                      1 = display books
                      2 = add books
                      3 = lend books
                      4 = return books
                    '''
            print(menu)
            choice = int(input("choose option "))
            if choice == 1:
                library.display_book()
            elif choice == 2:
                book = input("enter book name:")
                library.add_book(book)
            elif choice == 3:
                book = input("enter book name:")
                library.lend_book(book)
            elif choice == 4:
                book = input("enter book name:")
                library.return_book(book)
            else:
                print("enter correct choice")
        elif option == 'Q':
            accept = False
        else:
            print("enter correct option")

if __name__ == '__main__':
    main()


