
class Uditya_Library:
        def __init__(self):
                self.name = input("Enter your name: ")
                n = int(input("Enter the number of books do you want to add in library: "))
                self.book_list = []  # to store the books
                self.name_list = [] # to store the name of contributors
                i = 1
                while i<=n:
                        self.book = input(f"Enter the book-{i} in the book_list: ")
                        self.book_list.append(self.book)
                        i = i+1
                        
                 
                print("\t*****Thanks for your Contribution*****")
                print("\n") 
                f = open('71.1_Store_book.txt', "r+")
                f.write(f"Your Books Present in the library is:\n {self.book_list} ")

                f.close()     





        def add_book(self):
                '''Take the inputs from the user in form of the dictionary:
                dict = {}
                book = input()
                name = input()
                dict[book] = name
                print(dict)
                '''
                self.dict = dict()
                self.name_list = set()
                j = 1
                m = int(input("Enter the number of participants: "))

                while j<=m:
                        i = 1
                        name = input(f"Please Enter the name of Participents-{j}: ")
                        self.no_book = int(input("Please Enter the no of books do you want to add: "))
                        while i<=self.no_book:
                                book = input(f"Enter the name of the Book-{i} which you want to add in the library: ")
                                self.dict[book] = name
                                self.book_list.append(book)
                                i = i+1
                        print("\n")
                        self.name_list.add(name)
                        j = j+1

                f = open('71.2_Add_book.txt', "r+")
                f.write(f"Your books in the Liberary is: {self.dict}\n\n")
                f = open('71.1_Store_book.txt', "r+")
                f.write(f"Your books in the Liberary is: {self.book_list}\n\n")
                f.close()

        def lend_book(self):
                f = open("71.3_lend_book.txt",'r+')
                m = int(input("Please enter the no of books do you want to buy: ")) 
                i = 1
                while i<=m:
                        self.buy_book = input("Enter the book- name which you want to buy from the library: ") 
                        for books in self.book_list: 
                                if   (books == self.buy_book):
                                        self.book_list.remove(self.buy_book)
                                
                        i = i + 1
                # f = open('71.1_Store_book.txt', "r+")
                # f.write(self.book_list.remove(self.buy_book))
                f.write(f"Books which is lend by the student: {self.buy_book}")
                f.close()

        def return_book(self):
                pass          

        def display_book(self):
                print (f"Your books present in the library is: {self.book_list}")
                print(f"name of participants: {self.name_list}")
                print(f"list of the participants with the contibutions: {self.dict}")
                print("\n")

li = Uditya_Library()

while True:
        print(f"Please select the given options \n 1. for add the book in library: \n 2. for lend the book to the library: \n 3. for return the book to the library: \n 4. for display the book present in the library: \n 0. for Quit the loop: ")
        print("\n")


        n = int(input("Enter the options: "))

        if n == 1:
                li.add_book()
        
        elif n == 2:
                li.lend_book()

        elif n == 3:
                li.return_book()

        elif n == 4:
                li.display_book()

        elif n == 0:
                break
        else:
                print("Please Enter the given options only! **try again** \n")