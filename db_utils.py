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
def get_books_by_student_id():
    try:
        db_name = 'hogwarts_library'
        db_connection = _connect_to_db(db_name)
        print(f'Connected to database: {db_name}')

    except Exception as exc:
        print('Failed to read data from database')

    finally:
        if db_connection:
            db_connection.close()
            print('Connection closed')



def main():
    # RunQuery()
    get_books_by_student_id()


if __name__ == '__main__':
    main()