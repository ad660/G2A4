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


def main():
    get_all_books()
    get_books_by_student_id(10)


if __name__ == '__main__':
    main()
