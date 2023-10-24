import mysql.connector
from config import HOST, USER, PASSWORD


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


def get_all_students():
    try:
        db_name = 'hogwartslibrary'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to database: {db_name}')

        query = """ 
        SELECT s.* FROM students s
        """

        cur.execute(query)
        students = cur.fetchall()
        hogwarts_students = _map_students_values(students)
        print(hogwarts_students)
        cur.close()


    except Exception as exc:
        print(exc)

    finally:
        if db_connection:
            db_connection.close()
            print('Connection closed')

    return hogwarts_students

# GET BOOKS ON LOAN BY STUDENT ID
def _map_students_values(students_list):
    mapped = []
    for student in students_list:
        mapped.append(
            {
                'first_name': student[1],
                'last_name': student[2],
                'birthDate': student[3].strftime("%d-%m-%Y"),
                'house':student[4],
                'email': student[5],
                'join_date': student[6].strftime("%d-%m-%Y")
            }
        )
    return (mapped)




def RunQuery():
    conn = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database="hogwartslibrary")
    connection = conn.cursor()
    connection.execute("select * from books")
    results = connection.fetchall()
    items = []
    for row in results:
        items.append({'title': row[1], 'author': row[2], 'year_published': row[3],
                      'subject': row[4], 'description': row[5], 'age_restrict': row[6], 'stockID': row[7]})
    return items
  



def get_all_books():
    try:
        db_name = 'hogwartslibrary'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to database: {db_name}')

        query = """ 
        SELECT b.* FROM books b
        """

        cur.execute(query)
        results = cur.fetchall()
        books_in_library = []
        for item in results:
            books_in_library.append({'title': item[1], 'author': item[2],
                                     'year_published': item[3], 'subject': item[4],
                                     'description': item[5], 'age_restrict': item[6], 'stockID': item[7]})
        print(books_in_library)
        cur.close()

    except Exception as exc:
        print(exc)

    finally:
        if db_connection:
            db_connection.close()
            print('Connection closed')

    return books_in_library


# GET BOOKS ON LOAN BY STUDENT ID
def _map_values(student_loaned_books):
    mapped = []
    for item in student_loaned_books:
        mapped.append(
            {
                'studentID': item[0],
                'title': item[1],
                'author': item[2],
                'check out': item[3].strftime("%d-%m-%Y"),
                'return by': item[4].strftime("%d-%m-%Y")
            }
        )
    return mapped


def get_books_by_student_id(student_id):
    try:
        db_name = 'hogwartslibrary'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to database: {db_name}')

        query = """ 
        SELECT s.studentID, b.title, b.author, lb.checked_out_date, lb.return_date
        FROM students s
        JOIN loaned_books lb ON lb.studentID = s.studentID
        JOIN books b ON lb.bookID = b.bookID
        WHERE s.studentID = '{}'
        """.format(student_id)

        cur.execute(query)
        results = cur.fetchall()
        student_books_on_loan = _map_values(results)

        cur.close()

    except Exception as exc:
        print(exc)

    finally:
        if db_connection:
            db_connection.close()
            print('Connection closed')

    return student_books_on_loan

def add_new_book(title, author, year_published, subject, description, age_restrict, stockID):
    try:
        db_name = 'hogwartslibrary'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to database: {db_name}')

        query = """
        INSERT INTO books (title, author, year_published, subject, description, age_restrict, stockID)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        data = (title, author, year_published, subject, description, age_restrict, stockID)
        cur.execute(query, data)
        db_connection.commit()

        print(f'Book added successfully.')

    except Exception as e:
        print(f'Failed to add book. Error: {e}')

    finally:
        if db_connection:
            db_connection.close()
            print('Connection closed')


def add_student(first_name, last_name, birthDate, house, email, join_date):
    try:
        db_name = 'hogwartslibrary'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to database: {db_name}')

        query = """
                INSERT INTO students (first_name, last_name, birthDate, house, email, join_date)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
        cur.execute(query, (first_name, last_name, birthDate, house, email, join_date))
        db_connection.commit()
    except Exception as e:
        print(f'Failed to add student. Error: {e}')

    finally:
        if db_connection:
            db_connection.close()
            print('Connection closed')




def delete_graduated_students ():
    try:
        db_name = 'hogwartslibrary'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to database: {db_name}')

        query = """DELETE  s, lb FROM students s INNER JOIN loaned_books lb WHERE floor(datediff(now(),s.birthDate) / 
        365.25)  >= 18;
        SELECT * FROM students;
        """

        cur.execute(query)
        students = cur.fetchall()
        student_list = _map_students_values(students)
        cur.close()

        print(f'Students deleted successfully.')

    except Exception as e:
        print(f'Failed to add book. Error: {e}')

    finally:
        if db_connection:
            db_connection.close()
            print('Connection closed')
    return (student_list)


def main():
    get_all_books()
    get_books_by_student_id(10)
    add_student("K", "O", "1998-07-12", "Slytherin", "KO@example.com", "2023-10-24")


if __name__ == '__main__':
    main()
