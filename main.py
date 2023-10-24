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

    student_name = input("Welcome, what is your name? ")
    print(f"Welcome to the Hogwarts Library {student_name}!")
    student_id = int(input("To check out what books you current have out on loan please enter your student ID "))
    run_student_id_loaned_books(student_id)

    print("There are several options avaliable for you to choose from")
    print("If you would like to see all the books available please select option 1")
    print("To check out a book please enter Select option 2 and enter the ID of the book you would like to check out")
    print("(please note: one you check out a book it will be unavailable to other students)")
    student_chooses_option()


def student_chooses_option():
    select_option = int(input("Please choose your option now "))
    if select_option == 1:
        print("You have chosen to see all books available")
        return get_all_books()
    if select_option == 2:
        print("You have chosen to check out a book")
        book_id = int(input("Please enter the ID of the book you would like to check out"))
    if select_option is None or isinstance(select_option, (int, float)):
        print("Invalid option please enter option again ")
        student_chooses_option()



def display_student(students):
    for student in students.values:
        for item in student:
            print("{} {} {} {} {} {} {}".format(
            'Student ID: ' + item['studentID'],
            '\nfirst_name: ' + item['first_name'],
            '\nlast_name: ' + item['author'],
            '\nbirthDate: ' + item['birthDate'],
            '\nhouse ' + item['house'],
            '\nemail: ' + item['return by'],
            '\njoin date ' + item['join_date']
        ))


def run_delete_graduated_students():
    print ("Deleting all graduate student records... ")
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
    # run_student_id_loaned_books(6)
    welcome_to_library()
    # get_all_books()
    # get_student_id_loaned_books(6)

