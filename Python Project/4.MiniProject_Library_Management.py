'''Project to make a library Management system'''

class Library:
#     list1 = ["C","C++","Python","Java","Math","Physics"]
    def __init__(self):
        self.name = input("Enter your name: ")
        self.list = ["C","C++","Python","Java","Math","Physics"]
        self.list2 = self.list

    def display_book(self):
        return f"list of books which is present in your library: {self.list2}"
    


    def add_book(self):
        n = int(input("Enter the number of books do you want to add in Library: "))
        i = 0
        while(i<n):   
         self.add = input("Enter the name of book : ")
         self.list2.append(self.add)
         i = i+1

        print("Book is added...")
        return f"List of books in your library: {self.list2}"
    
    def lend_book(self):
        n = int(input("Enter the number of books do you want to buy:"))
        i = 0
        while(i<n):   
         self.buy = input("Enter the name of book: ")
         i = i+1
        
        for element in self.list2:
            if (element == self.buy):
             i = 0
             while(i<n):
                print( f"You bought the {self.buy} book")
                self.list2.remove(element)
                i= i+1
                print(f"List of books in your library: {self.list2}")
             break
        else:
            print("This Book is not present in the library: ")
            print(f"Present books in your Library is : {self.list2}")
    
    def restore_book(self):
       self.restore = input("Return the buy book to the Library: ")
       self.list2.append(self.restore)
       print(f"Reurning the {self.buy} book: \n Your Library book list is: {self.list2}") 
    

print(" ")
print("**********Welcome to the Library managment system:**********")
print(" ")
li = Library()
i = 0
while(True):
   print(f"Enter the Number to Proceed ==> \n 1 for add the book in Library:\n 2 for buy the book from the Library:\n 3 for return the book to the Library:\n 4 for Display the books present in the Library:\n 0 for quit the Library")
   print(" ")
   n = int(input("Enter the number: "))
   if n == 1:
      print(li.add_book())
      print(" ")
    
   elif n == 2:
      print(li.lend_book())
      print(" ")
  
   elif n == 3:
      print(li.restore_book())
      print(" ")
    
   elif n == 4:
      print(li.display_book())
      print(" ")
  
   else:
      print("Quiting the Library:==> *****Have a nice day****")
      break
