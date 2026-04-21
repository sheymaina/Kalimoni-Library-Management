
# Kalimoni Library Console

A Python command-line application that simulates a library management system using Object-Oriented Programming. 
 Features
- Book Management: Add books with title, author, and ISBN
- Member Management: Register library members with unique IDs
- Borrow/Return System: Members can borrow available books and return them
- State Tracking: View current status of all books and members at any time
- Validation: Prevents borrowing books that are already checked out

 Project Structure
 Book  Stores book details and tracks borrowing status 
 Class  Responsibility  Book  Stores book details and tracks borrowing status 
 Member  Stores member info and list of borrowed books 
 Library  Manages books/members and handles borrow/return operations 



Books:
- Things Fall Apart by Chinua Achebe | ISBN: 978-0435905255 | Available
-  - The River Between by Ngugi wa Thiong'o | ISBN: 978-0435905484 | Available


How It Works
1. Initialize Library: Create a Library instance with a name
2. Populate Data: Add Book and Member objects to the library
3. Operations: Call borrow_book(isbn, member_id) or return_book(isbn, member_id)
4. Check Status: Use print_state() to see all books and members


 Author
Esther Maina
