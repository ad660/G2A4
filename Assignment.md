Hogwarts book library 

SQL Tables 
- Student information table 
    - Student ID
    - Student Name 
    - Student House 
    - Student Age 


- Books table 
    - Book ID
    - Name 
    - Author 
    - Subject
    - Description 

- Stock level table 
    - Foreign key: Book Table ID 
    - Book level 

 - Loaned Books table (books that are loaned out)
    - Foreign Key: Book ID
    - Foreign Key: Student ID
    - Date of check out 


Functionality 

- Sign up/Sign in (checks if student = yes)
- Check all books 
  - Function then checks whether the book is on loan or not 
  - if onLoan = 'yes' then tell the student 
  - if onLoan = 'No' then asks if the student wants to check out the book
    - if student selects 'yes' set bookCheckedOut to 'yes' and UPDATE Loaned Books SQL Table 
    - Show updated SQL table to reflect that student has checked out book 