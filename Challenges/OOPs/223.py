# Book Details

class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.auther = author
        self.price = price
    
    def show_details(self):
        print('Title:',self.title)
        print('Auther:',self.auther)
        print('Price:',self.price)

b1 = Book('Python Crash Course','Eric Mathews',1000)
b2 = Book('Learn Python','Mark Lutz',500)

print(b1.show_details())
print(' ')
print(b2.show_details())