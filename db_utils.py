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

def RunQuery():
    conn=mysql.connector.connect(host="localhost",user="root",password="Zenjie12!",database="Hogwarts_Library")
    connection=conn.cursor()
    connection.execute("select * from books")
    results=connection.fetchall()
    items=[]
    for row in results:
        items.append({'title':row[1],'author': row[2],'year_published':row[3],'subject':row[4],'description':row[5],'age_restrict':row[6],'stockID':row[7]})
    return items


## GET BOOKS ON LOAN BY STUDENT ID
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

# sample query to make sure we're connected to DB
def get_books_by_student_id(student_id):
    try:
        # connecting to database (always the SAME!)
        db_name = 'hogwartslibrary'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to database: {db_name}')

        # executing query (SQL syntax in """ [SQL] """)
        query = """ 
        SELECT s.studentID, b.title, b.author, lb.checked_out_date, lb.return_date
        FROM students s
        JOIN loaned_books lb ON lb.studentID = s.studentID
        JOIN books b ON lb.bookID = b.bookID
        WHERE s.studentID = '{}'
        """.format(student_id)

        cur.execute(query)
        results = cur.fetchall()

        for i in results:
            print(i)

        cur.close()

    except Exception:
        print('Failed to read data from database')

    finally:
        if db_connection:
            db_connection.close()
            print('Connection closed')



def main():
    # RunQuery()
    get_books_by_student_id(10)


if __name__ == '__main__':
    main()