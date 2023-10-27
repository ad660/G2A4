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


def _map_students_values(students_list):
    mapped = []
    for student in students_list:
        mapped.append(
            {
                'studentID': student[0],
                'first_name': student[1],
                'last_name': student[2],
                'birthDate': student[3],
                'house': student[4],
                'email': student[5],
                # 'join_date': student[6].strftime("%d-%m-%Y")
            }
        )
    return mapped


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
        cur.close()

    except Exception as exc:
        print(exc)

    finally:
        if db_connection:
            db_connection.close()
            print('Connection closed: get students')

    return hogwarts_students


def _map_all_book_values(all_books):
    mapped = []
    for item in all_books:
        mapped.append(
            {
                'bookID': item[0],
                'title': item[1],
                'author': item[2],
                'year_published': item[3],
                'subject': item[4],
                'description': item[5],
                'age_restrict': item[6]
            }
        )
    return mapped


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
        books_in_library = _map_all_book_values(results)
        cur.close()

    except Exception as exc:
        print(exc)

    finally:
        if db_connection:
            db_connection.close()
            print('Connection closed: get all books')

    return books_in_library


def _map_studentids(result):
    mapped = []
    for item in result:
        mapped.append(
            {
                'studentID': item[0]
            }
        )
    return mapped


def get_students_ids():
    try:
        db_name = 'hogwartslibrary'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to database: {db_name}')

        query = """ 
        SELECT s.studentID
        FROM students s
        JOIN loaned_books lb ON lb.studentID = s.studentID
        """

        cur.execute(query)
        student_ids = cur.fetchall()
        mapped_student_ids = _map_studentids(student_ids)
        cur.close()

    except Exception as exc:
        print(exc)

    finally:
        if db_connection:
            db_connection.close()
            print('Connection closed: get students IDs')

    return mapped_student_ids


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
            print('Connection closed: get loaned books/studentID')

    return student_books_on_loan


def add_new_book(title, author, year_published, subject, description, age_restrict):
    try:
        db_name = 'hogwartslibrary'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to database: {db_name}')

        query = """
                INSERT INTO books (title, author, year_published, _subject, _description, age_restrict)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
        cur.execute(query, (title, author, year_published, subject, description, age_restrict))

        cur.execute("SELECT LAST_INSERT_ID()")
        bookID = cur.fetchone()[0]

        stock_quantity = 1
        cur.execute("""
                    INSERT INTO book_stock (stock_quantity, stock_available, bookID)
                    VALUES (%s, %s, %s)
                    """, (stock_quantity, 1, bookID))

        db_connection.commit()
    except Exception as exc:
        print(f'Failed to add book. Error: {exc}')

    finally:
        if db_connection:
            db_connection.close()
            print('Connection closed: add new book')


def add_new_student(first_name, last_name, birthDate, house, email, join_date):
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
            print('Connection closed: add new student')


# def delete_graduated_students():
#     try:
#         db_name = 'hogwartslibrary'
#         db_connection = _connect_to_db(db_name)
#         cur = db_connection.cursor()
#         print(f'Connected to database: {db_name}')
#
#         query = """DELETE  s, lb FROM students s INNER JOIN loaned_books lb WHERE floor(datediff(now(),s.birthDate) /
#         365.25)  >= 18;
#         SELECT * FROM students;
#         """
#
#         cur.execute(query)
#         students = cur.fetchall()
#         student_list = _map_students_values(students)
#         cur.close()
#
#         print(f'Students deleted successfully.')
#
#     except Exception as e:
#         print(f'Failed to add book. Error: {e}')
#
#     finally:
#         if db_connection:
#             db_connection.close()
#             print('Connection closed: delete grad student')
#     return (student_list)


def run_db_utils():
    get_all_students()
    get_all_books()
    get_students_ids()
    get_books_by_student_id(6)



if __name__ == '__main__':
    run_db_utils()
