import requests
import json
from db_utils import _connect_to_db



# -- RUN: GET LOANED BOOKS BY STUDENT ID --

def get_all_books():
    try:
        url = 'http://127.0.0.1:5000/books'
        result = requests.get(url)
        if result.status_code == 200:
            data = result.json()
            if isinstance(data, dict):
                for key, value in data.items():
                    print(f"{key}: {value}")
            else:
                raise Exception("Invalid data format: Data should be a dictionary.")
        else:
            raise Exception(f'Request failed with status code: {result.status_code}')
    except Exception as e:
        print(f'Error occurred: {e}')

    # Call the function to display all the books in the console

    # try:
    #     url = 'http://127.0.0.1:5000/books'
    #     result = requests.get(url)
    #     if result.status_code == 200:
    #         data = result.json()
    #         return data
    #     else:
    #         raise Exception(f'Request failed with status code: {result.status_code}')
    # except Exception as e:
    #     print(f'Error occurred: {e}')
    #     return None

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

def run_student_id_loaned_books(student_id):
    # student_id = input('You would like to check the loaned books of a student? What is their Student ID:  ')
    loaned_books = get_student_id_loaned_books(int(student_id))
    display_loaned_books(loaned_books)
# -- END: GET LOANED BOOKS BY STUDENT ID --

# def librarian_adds_a_book():
#     print('Please enter what books you\'d like to add to the library')
#     enterBook = input('Please enter the title, author, year published, subject, description')
#     add_new_book(enterBook)


def welcome_to_library():
    print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣷⡀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⣸⣽⣿⣽⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣷⡀⠀⠀⠀⠀⠀⠀⣼⣇⠀⢸⣿⣿⣿⣿⡏⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣧⠀⠀⠀⠀⠀⢰⣿⣿⡀⢸⣿⣿⢻⣿⡇⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣛⣿⣻⠀⠀⠀⠀⠀⢸⣿⣿⠀⢸⣿⣿⣾⣿⡇⢀⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣧⡀⠀⠀⠀⠀⣿⣿⣿⣷⢸⣿⣿⣿⣿⣇⣀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⢿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣼⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⢠⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⣿⣿⠀⠀⢰⡄⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⢧⢤⢤⢤⢼⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣀⣀⣀⣾⡿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠻⣿⢿⡿⠇⠀⣼⣧⠀⠀⠀⠀⣀⣀⣀⣸⣿⣿⣿⣿⣿⣾⣾⣾⣾⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣷⣷⣿⣷⣿⠄⠀⠀⠀⠀⠀⠀⡷⠶⠆⠀⠀
⠀⢾⣿⣿⣿⡇⢰⣿⣿⡄⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⣿⣿⢿⣿⡇⢸⣿⣿⡃⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣛⣿⣿⣼⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣠⣧⠀⠀⠀⠀
⠹⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣰⣿⣿⣧⡀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⡿⣿⣿⡿⣿⣿⠿⣿⣿⠿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣏⣿⠃⠀⠀⠀⣰⣿⣿⣿⣿⣷⡀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⡟⠀⣿⣿⡇⣿⣿⠀⣿⣿⠀⣿⣿⠀⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⠃⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣧⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⢸⣿⣿⢻⣿⣿⣷⡄
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢀⠀⣸⣿⣿⣾⣿⣿⣯⡇
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠸⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⣤⣠⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣄⠀⠐⣾⢴⣄⣠⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⢸⣿⢀⣠⡴⠲⣦⠀⣾⡇⢸⣿⠀⢸⣿⠀⣤⠀⢻⡇⠙⠁⣿⡇⠀⣿⠘⠉⢸⣿⠀⢀⡠⢶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣀⣿⣿⣀⣼⣿⠉⢹⣇⠀⣿⡇⣿⡇⢀⣿⠀⢸⣿⠀⣿⠀⣿⡇⣾⡇⣿⡇⠀⣿⠀⠀⢸⣿⠀⠙⢷⣜⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⢸⣿⠀⠸⣿⠀⣿⠇⠛⠷⠋⣿⠀⠘⢿⡼⠻⣴⠋⠀⠸⠷⠿⠋⠀⠛⠀⠀⢸⣿⠀⢴⡆⢻⡦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠀⢸⣿⠀⠀⠈⠉⠁⠀⣀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠀⠀⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠛⠂⠀⠀⠀⠀⠀⢿⡦⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')

    librarian_name = input("Warm welcome back Hogwartian Librarian! Please sign in with your name: ")
    print(f"Welcome to the Hogwarts Library {librarian_name}!")
    print('There are multiple students with books on loan, their student ID\'s are: 6, 10, 12')
    student_id = int(input("To check out what books a student currently have on loan please "
                           "enter the number of their student ID : "))
    run_student_id_loaned_books(student_id)
    student_chooses_option()


def student_chooses_option():
    print("If you would like to see all the books available please now select option 1: ")
    select_option = int(input("Please choose your option now: "))

    if select_option == 1:
        print("You have chosen to see all books available")
        return get_all_books()
    elif select_option is None or isinstance(select_option, (int, float)):
        print("Invalid option please enter option again ")
        student_chooses_option()



def display_student(students):
    student_data = students['Students']
    for item in student_data:
        print(
            "---------------------------"

            '\nStudent ID: ' + str(item['studentID']),
            '\nfirst_name: ' + item['first_name'],
            '\nlast_name: ' + item['last_name'],
            '\nhouse ' + item['house'],
            '\nemail: ' + item['email'],
            '\njoin date ' + item['join_date'],

            "\n---------------------------"
        )

def run_view_all_students():
    # try:
    url = f'http://127.0.0.1:5000/students'
    result = requests.get(url)
    if result.status_code == 200:
        data = result.json()
        print("Displaying Students data: ")
        display_student(data)
        return data
    else:
        raise Exception(f'Request failed with status code: {result.status_code}')
    # except Exception as e:
    #     print(f'Error occurred: {e}')
    #     return None



if __name__ == '__main__':
    welcome_to_library()

