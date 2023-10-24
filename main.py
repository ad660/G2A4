import requests
import json


 @app.route('/books', methods=['GET'])
 def get_books():
     if request.method=='GET':
         data={"data":"testing"}
         return jsonify(data)


# -- RUN: GET LOANED BOOKS BY STUDENT ID --
def get_student_id_loaned_books(student_id):
    try:
        url = f'http://127.0.0.1:5000/books_on_loan/{student_id}'
        result = requests.get(url)
        if result.status_code == 200:
            data = result.json()
            return data
        else:
            raise Exception(f'Request failed with status code: {result.status_code}')
    except Exception as e:
        print(f'Error occurred: {e}')
        return None


def display_loaned_books(result):
    for item in result:
        print("{} {} {} {} {}".format(
            'Student ID: ' + str(item['studentID']),
            '\nTitle: ' + str(item['title']),
            '\nAuthor: ' + str(item['author']),
            '\nChecked Out Date: ' + str(item['check out']),
            '\nReturn By Date: ' + str(item['return by'])
        ))


def run_student_id_loaned_books():
    student_id = input('You would like to check the loaned books of a student? What is their Student ID:  ')
    loaned_books = get_student_id_loaned_books(int(student_id))
    display_loaned_books(loaned_books)
# -- END: GET LOANED BOOKS BY STUDENT ID --


if __name__ == '__main__':
    run_student_id_loaned_books()
    