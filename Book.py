# Aiden Munger
# 1/29/2026
# Book class Demo OOP
# Library System

class Book:
    def __init__(self, title : str, checked_out : bool = False):
        self.title = title
        self.checked_out = checked_out
        
    def check_out(self):
        self.checked_out = True
    
    def return_book(self):
        self.checked_out = False

    def __str__(self):
        str_rep = f"{self.title}, checked out: {self.checked_out}"
        
        return str_rep
    
hp1 = Book("Harry Potter and the Sorcerer's Stone")
print(hp1)
hp1.check_out()
print(hp1)

hp1.return_book()
print(hp1)