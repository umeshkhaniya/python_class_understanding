# Multiple inheritance by calling the super.
# Here we need to call using: super().__init__(title, price) # this will call the first parent class.
                                                                # or super(Book, self).__init__(title, price)
#                             super(Publication, self).__init__(period, publisher) # this will call the nect class 
                                                                                    # after Publication
# you can call also call parent class without using super as  using: Publication.__init__(self)



class Publication:
    def __init__(self, title, price):
        print("Pub Initialized")
        self.title = title
        self.price = price


class Periodical:
    def __init__(self, publisher, period):
        print("Peri Initialized")
        self.period = period
        self.publisher = publisher


class Book(Publication, Periodical):
    def __init__(self, title, publisher, period, author, pages, price):
        super().__init__(title, price)
        super(Publication, self).__init__(period, publisher)
        self.author = author
        self.pages = pages

        print("uk")



class Book1(Publication, Periodical):
    """This will not work as we need to call all  the parameters from parent class
    """
    def __init__(self, title, publisher, author, pages, price):
        super(Book1, self).__init__(title, price) # is same as super().__init__(title, price)
        super(Publication, self).__init__(publisher)
        self.author = author
        self.pages = pages

        print("uk")







b1 = Book("Brave New World", "Springer Nature", "Daily", "Aldous Huxley", 311, 10)

print(b1.author)

b2 = Book1("Brave New World", "Springer Nature",  "Aldous Huxley", 311, 10) # this will not work as we need to take all 
                                                                            # the parameters from parent class while defining the Book1






