class Publication:
    def __init__(self, title, author):       
        self.title = title
        self.author = author 
        # this first part will make the superclass/base class/ parent class which is Publication

    def set_title(self,title):
        self.title = title # sets publication title

    def get_title(self):
        return self.title # returns publication title

    def set_author(self, author):
        self.author = author #sets publication author

    def get_author(self):
        return self.author # returns publication author

    # 1: as indicated in the previous study guide(sg 8 - encapsulation), the setter will update the value of the attribute, - updates/changes
    # 2: while the getter will retreieve or basically get the value of that attrbute - reads

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        # this part will display the title and author of the publication

class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author) # this part shows that this new class (Book) will inherit the title and author attributes of the Parent Class 'Publication'
        self.number_of_pages = number_of_pages # this is the new attribute of the child class Book, therefore,it will inherit attributes from the base class but will also have its own

    def set_number_of_pages(self, number_of_pages): # this part will check if  the number of pages of the book is less than or equal to zero
        if number_of_pages > 0:
             self.number_of_pages = number_of_pages
        else:
            print("The number of pages must be positive.")
           
    def get_number_of_pages(self):
        return self.number_of_pages
        # this part will return the number of pages of the book
        
    def display_info(self):
        super().display_info() # since this is inherited, this will display the title and author of the book
        print(f"Number of Pages: {self.number_of_pages}")
    # this will display the number of pages of the book provided

class Magazine(Publication): 
    def __init__(self, title, author, issue_number):
        super().__init__(title, author) # same as the one above, this part shows that the attributes title and author from the paernt class Publication will be inherited by the child class Magazine
        self.issue_number = issue_number # an attribute of its own --- an additional attribute other than the ones inherited form the Parent Class

    def set_issue_number(self, issue_number): # this part wll also check if the value given is less than or equal to zero
        if issue_number > 0:
            self.issue_number = issue_number
        else:
            print("The issue number must be positive.")

    def get_issue_number(self):
        return self.issue_number
        # will also return the issue number of the magazine

    def display_info(self):
        super().display_info() # inherited from the parent class, so it wil show title and author of the magazine provided
        print(f"Issue Number: {self.issue_number}")
    # this will display the issue number of the magazine
    
# using the sample objects from SG to confirm if the output will be the same

pub1 = Publication ("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine ("National Geographic", "Various Authors", 202)

#printing info 

print("Publication Information:")
pub1.display_info() #this was defined earlier in the publication class, so this will show or display the title and author attribute inputs

print("\nBook Information:")
book1.set_number_of_pages(-310) #will show the message as the code required a positive number
book1.display_info() #will show title and author (attributes inherited from parent class)

print("\nMagazine Information:")
mag1.display_info() #will show title and author (attributes inherited from parent class)

    
    