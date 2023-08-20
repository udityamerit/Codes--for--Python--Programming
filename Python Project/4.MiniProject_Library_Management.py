'''Project to make a library Management system
Using OOPs '''

class Library:
#     list1 = ["C","C++","Python","Java","Math","Physics"]
    def __init__(self):
        self.list = ["C","C++","Python","Java","Math","Physics"]
        self.list2 = self.list

    def display_book(self):
        return f"list of books which present in the library: {self.list2}"


    def add_book(self):
        n = int(input("Enter the number of books do you want to add in Library: "))
        i = 0
        while(i<n):   
         self.add = input("Enter the name of book : ")
         self.list2.append(self.add)
         i = i+1

        print("Book is added...")
        return f"List of books in the library: {self.list2}"
    
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
                i= i+1
             break
        else:
            print("This Book is not present in the library: ")
            print(f"Present books in the Library is : {self.list2}")

        
    
li = Library()
print(li.display_book())
print(" ")

print(li.add_book())
print(" ")

print(li.lend_book())
print(" ")
