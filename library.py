#import library
class Book:
    def _init_(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrowed_by = None
    
    def _str_(self):
        status = f"Borrowed by {self.borrowed_by}" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | {status}"


class Member:
    def _init_(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def _str_(self):
        books = ", ".join([book.title for book in self.borrowed_books]) or "None"
        return f"Member: {self.name} | ID: {self.member_id} | Books: {books}"


class Library:
    def _init_(self, name):
        self.name = name
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title}")
    
    def add_member(self, member):
        self.members.append(member)
        print(f"Added member: {member.name}")
    
    def borrow_book(self, isbn, member_id):
        book = self._find_book(isbn)
        member = self._find_member(member_id)
        
        if not book:
            print(f"Book with ISBN {isbn} not found.")
            return
        if not member:
            print(f"Member with ID {member_id} not found.")
            return
        if book.is_borrowed:
            print(f"'{book.title}' is already borrowed by {book.borrowed_by}.")
            return
            
        book.is_borrowed = True
        book.borrowed_by = member.name
        member.borrowed_books.append(book)
        print(f"{member.name} borrowed '{book.title}'")
    
    def return_book(self, isbn, member_id):
        book = self._find_book(isbn)
        member = self._find_member(member_id)
        
        if not book or not member:
            print("Book or member not found.")
            return
        if book not in member.borrowed_books:
            print(f"{member.name} did not borrow '{book.title}'.")
            return
            
        book.is_borrowed = False
        book.borrowed_by = None
        member.borrowed_books.remove(book)
        print(f"{member.name} returned '{book.title}'")
    
    def print_state(self):
        print(f"\n--- {self.name} State ---")
        print("\nBooks:")
        for book in self.books:
            print(f"  - {book}")
        print("\nMembers:")
        for member in self.members:
            print(f"  - {member}")
        print("-" * 30)
    
    def _find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def _find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

#Program
def main():

    lib = Library("Kalimoni Community Library")
    
    #books
    lib.add_book(Book("Things Fall Apart", "Chinua Achebe", "978-0435905255"))
    lib.add_book(Book("The River Between", "Ngugi wa Thiong'o", "978-0435905484"))
    lib.add_book(Book("Born a Crime", "Trevor Noah", "978-0399588174"))
    
    #members
    lib.add_member(Member("Esther Wanjiku", "M001"))
    lib.add_member(Member("Noah Kimani", "M002"))
    
    #Initial state
    lib.print_state()
    
    # Perform operations
    print("\n--- Performing Operations ---")
    lib.borrow_book("978-0435905255", "M001")  
    lib.borrow_book("978-0399588174", "M002")  
    lib.borrow_book("978-0435905255", "M002")  
    
    #after borrowing
    lib.print_state()
    
    #Return book
    print("\n--- Returning Books ---")
    lib.return_book("978-0435905255", "M001")  
    
    #Final state
    lib.print_state()



    


        
    