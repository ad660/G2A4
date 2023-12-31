DROP DATABASE IF EXISTS hogwartslibrary;
CREATE DATABASE hogwartslibrary;
USE hogwartslibrary;

-- Create a table to store information about books
CREATE TABLE books (
    bookID INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255),
    year_published INT,
    _subject VARCHAR(50),
    _description VARCHAR(500),
    age_restrict INT
);

-- Create a table to track book stock levels
CREATE TABLE book_stock (
    stockID INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
    stock_quantity INT NOT NULL,
    stock_available INT DEFAULT 0,
    bookID INT,
    FOREIGN KEY (bookID) REFERENCES books(bookID)
);

-- Create a table to store information about students
CREATE TABLE students (
    studentID INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birthDate DATE NOT NULL,
    house VARCHAR(20),
    join_date DATE NOT NULL
);

-- Create a table to store information about books on loan
CREATE TABLE loaned_books (
    loanID INT AUTO_INCREMENT PRIMARY KEY,
    bookID INT,
    studentID INT,
    checked_out_date  DATE,
    return_date DATE,
    FOREIGN KEY (bookID) REFERENCES books(bookID),
    FOREIGN KEY (studentID) REFERENCES students(studentID)
);

INSERT INTO books (title, author, year_published, _subject, _description, age_restrict)
VALUES
    ('Fantastic Beasts and Where to Find Them', 'Newt Scamander', 2001, 'Magizoology', 'A guide to magical creatures', 11),
    ('The Standard Book of Spells', 'Miranda Goshawk', 1990, 'Spellbook', 'A basic guide to spellcasting', 11),
    ('Quidditch Through the Ages', 'Kennilworthy Whisp', 1999, 'Sports', 'The history of Quidditch', 5),
    ('The Dark Forces: A Guide to Self-Protection', 'Quentin Trimble', 1980, 'Defense Against the Dark Arts', 'Defending against dark magic', 16),
    ('Hogwarts: A History', 'Bathilda Bagshot', 2005, 'History', 'The history of Hogwarts', 11),
    ('Magical Drafts and Potions', 'Arsenius Jigger', 2002, 'Potions', 'A guide to potion-making', 11),
    ('A History of Magic', 'Bathilda Bagshot', 1899, 'History', 'The history of wizardry', 11),
    ('Standard Book of Spells, Grade 3', 'Miranda Goshawk', 2000, 'Spellbook', 'An Intermediate\'s spellbook', 14),
    ('The Tales of Beedle the Bard', 'Beedle the Bard', 1640, 'Fairy Tales', 'Wizarding fairy tales', 3),
    ('Quintessence: A Quest', 'Unknown', 2002, 'Magical Philosophy', 'A philosophical exploration', 11);


INSERT INTO book_stock (stock_quantity, stock_available, bookID)
VALUES
    (3, 2, 1),
    (6, 4, 2),
    (3, 0, 3),
    (1, 1, 4),
    (5, 3, 5),
    (3, 2, 6),
    (2, 1, 7),
    (20, 11, 8),
    (2, 0, 9),
    (1, 1, 10);
     

    INSERT INTO students (first_name, last_name, birthDate, house, join_date)
VALUES

    ('Harry', 'Potter', '1980-07-01', 'Gryffindor', '1991-09-01'),
    ('Hermione', 'Granger', '1979-09-19', 'Gryffindor', '1991-09-01'),
    ('Ron', 'Weasley', '1980-03-01', 'Gryffindor','1991-09-01'),
    ('Draco', 'Malfoy', '1980-06-05', 'Slytherin', '1991-09-01'),
    ('Luna', 'Lovegood', '1981-02-13', 'Ravenclaw','1992-09-01'),
    ('Cedric', 'Diggory', '1978-09-07', 'Hufflepuff', '1989-09-01'),
    ('Ginny', 'Weasley', '1981-08-11', 'Gryffindor', '1992-09-01'),
    ('Cho', 'Chang', '1979-04-07', 'Ravenclaw', '1990-09-01'),
    ('Neville', 'Longbottom', '1980-07-30', 'Gryffindor', '1991-09-01'),
    ('Pansy', 'Parkinson', '1980-08-01', 'Slytherin', '1991-09-01'),
    ('Fred', 'Weasley', '1978-04-01', 'Gryffindor','1989-09-01'),
    ('George', 'Weasley', '1978-04-01', 'Gryffindor', '1989-09-01'),
    ('Seamus', 'Finnigan', '1980-07-14', 'Gryffindor', '1990-09-01'),
    ('Lavender', 'Brown', '1980-06-13', 'Gryffindor', '1991-09-01'),
    ('Padma', 'Patil', '1980-04-19', 'Ravenclaw', '1991-09-01'),
    ('Parvati', 'Patil', '1980-02-05', 'Gryffindor', '1991-09-01'),
    ('Blaise', 'Zabini', '1979-11-01', 'Slytherin',  '1991-09-01'),
    ('Justin', 'Finch-Fletchley', '1980-01-01', 'Hufflepuff', '1990-09-03'),
    ('Ernie', 'Macmillan', '1980-04-22', 'Hufflepuff', '1992-09-01'),
    ('Susan', 'Bones', '1980-08-21', 'Hufflepuff', '1991-09-01'),
    ('Millicent', 'Bulstrode', '1980-09-05', 'Slytherin',  '1991-09-01'),
    ('Hannah', 'Abbott', '1980-04-12', 'Hufflepuff', '1992-09-01'),
    ('Vincent', 'Crabbe', '1980-05-02', 'Slytherin', '1980-09-01'),
    ('Gregory', 'Goyle', '1979-11-02', 'Slytherin', '1979-09-01');
    

INSERT INTO loaned_books (bookID, studentID, checked_out_date, return_date)
VALUES
	(1, 6, '2023-10-14', '2023-10-28'),
    (3, 6, '2023-10-14', '2023-10-28'),
    (9, 6, '2023-10-14', '2023-10-28'),
    (2, 10, '2023-10-16', '2023-10-30'),
    (2, 12, '2023-10-15', '2023-10-29'),
	(4, 14, '2023-10-14', '2023-10-28'),
    (4, 15, '2023-10-14', '2023-10-28');

    
SELECT * FROM books;
SELECT * FROM book_stock;
SELECT * FROM students;
SELECT * FROM loaned_books;

