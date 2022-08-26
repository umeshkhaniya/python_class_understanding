# Understanding the Multiple inheritance
""" 
Defining the super in each base class so that you don't need to call the base class in your child class using super.
"""

# Here if we do the below like than will through the error as we supply the . 
# this will not work as our base init class only take two parameters but in child class super().__init__ we call the  
# four parameters. so we need to used **kwargs.
# including self total: 5 parameters




class Publication:
    def __init__(self, title, price):
        print("Pub Initialized")
        super().__init__()
        self.title = title
        self.price = price
        


class Periodical:
    def __init__(self, publisher, period):
        print("Peri Initialized")
        super().__init__()
        self.period = period
        self.publisher = publisher
        



class Book(Publication, Periodical):
    def __init__(self, title, publisher, period, author, pages, price):
        super().__init__(title, publisher, period, price) # this will not work as our base init class only take two parameters.
        # so we need to used *kwargs.

        self.author = author
        self.pages = pages

        print("uk")



# This will through the error.



b1 = Book("Brave New World", "Springer Nature", "Daily", "Aldous Huxley", 311, 10)




print(b1.author)

