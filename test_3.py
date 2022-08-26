# Understanding the Multiple inheritance
""" 
How to work for parmaeters without compalining the test_2.py.
Class 
Solving test_2.py issues.
"""

"""
Problem here is you need to call all the base class parameters.
"""



class Publication:
    def __init__(self, title, price, **kwargs):
        print("Pub Initialized")
        super().__init__(**kwargs)
        self.title = title
        self.price = price
        


class Periodical:
    def __init__(self, publisher, period, **kwargs):
        print("Peri Initialized")
        super().__init__(**kwargs)
        self.period = period
        self.publisher = publisher




class Book(Publication, Periodical):
    def __init__(self, title, publisher, period, author, pages, price):
        super().__init__(title = title, publisher = publisher, period = period, price = price) # this will not work as our base init class only take two parameters.
        # so we need to used *kwargs.

        self.author = author
        self.pages = pages

        print("uk")



# This will through the error.



b1 = Book("Brave New World", "Springer Nature", "Daily", "Aldous Huxley", 311, 10)




print(b1.author)

