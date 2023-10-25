import requests


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
    print(f"Welcome to the Hogwarts Library {librarian_name.title()}!")
    print()
    librarian_chooses_option()


def librarian_chooses_option():
    view_librarian_options()
    select_option = input("Please choose your option now: ")
    if select_option == str(1):
        print("You have chosen to see all books available.")
        return run_get_all_books()
    elif select_option == str(2):
        print("You have chosen to see all students.")
        return run_view_all_students()
    elif select_option == str(3):
        print("You have chosen to see loaned books by student ID.")
        return run_student_id_loaned_books()
    elif select_option == str(4):
        print("You have chosen to add a new student's information to the database.")
        return  # librarian_adds_a_student()
    elif select_option == str(5):
        print("You have chosen to add a new book to the database.")
        return  # librarian_adds_a_book()
    elif select_option is None or isinstance(select_option, (int, float)):
        print("Invalid option please enter option again ")
    else:
        print()
        print('There seems to have been an error please select again.')
        print()


def view_librarian_options():
    print('There are a variety of options available for you to choose from:')
    print("Select option 1 to see all the books available. [1]")
    print("Select option 2 to see all students. [2]")
    print("Select option 3 to see a students loaned books by Student ID. [3]")
    print("Select option 4 to add a new student. [4]")
    print("Select option 4 to add a new student. [5]")
    print()


def display_all_books(result):
    for key, values in result.items():
        for value in values:
            print("{} {} {} {} {} {} {} {}".format(
                'Book ID: ' + str(value['bookID']),
                '\nTitle: ' + str(value['title']),
                '\nAuthor: ' + str(value['author']),
                '\nyear_published: ' + str(value['year_published']),
                '\nsubject: ' + str(value['subject']),
                '\ndescription: ' + str(value['description']),
                '\nage_restrict: ' + str(value['age_restrict']),
                '\nstockID: ' + str(value['stockID'])
                )
            )
            print('-' * 50)


def run_get_all_books():
    try:
        url = 'http://127.0.0.1:5000/books'
        result = requests.get(url)
        if result.status_code == 200:
            data = result.json()
            return display_all_books(data)
        else:
            raise Exception(f'Request failed with status code: {result.status_code}')
    except Exception as e:
        print(f'Error occurred: {e}')


def display_all_students(result):
    for key, values in result.items():
        for value in values:
            print("{} {} {}".format(
                'Student ID: ' + str(value['studentID']),
                '\nFirst Name: ' + str(value['first_name']),
                '\nLast Name: ' + str(value['last_name']),
                # '\nhouse ' + str(item['house']),
                # '\nemail: ' + str(item['email']),
                # '\njoin date ' + str(item['join_date']),
                )
            )
            print('-' * 30)


def run_view_all_students():
    try:
        url = f'http://127.0.0.1:5000/students'
        result = requests.get(url)
        if result.status_code == 200:
            data = result.json()
            return display_all_students(data)
        else:
            raise Exception(f'Request failed with status code: {result.status_code}')
    except Exception as e:
        print(f'Error occurred: {e}')
        return None


def display_loaned_books(result):
    # for key, values in result.items():
    for value in result:
        print('-' * 30)
        print("{} {} {} {} {}".format(
            'Student ID: ' + str(value['studentID']),
            '\nTitle: ' + str(value['title']),
            '\nAuthor: ' + str(value['author']),
            '\nChecked Out Date: ' + str(value['check out']),
            '\nReturn By Date: ' + str(value['return by'])
            )
        )
        print('-' * 30)


def get_student_id_loaned_books(student_id):
    try:
        url = f'http://127.0.0.1:5000/books_on_loan/{student_id}'
        result = requests.get(url)
        if result.status_code == 200:
            data = result.json()
            return display_loaned_books(data)
        else:
            raise Exception(f'Request failed with status code: {result.status_code}')
    except Exception as e:
        print(f'Error occurred: {e}')
        return None


def run_student_id_loaned_books():
    print('There are currently multiple students with books on loan, their student ID\'s are: 6, 10, 12')
    student_id = input('To view what books a student currently has on loan please enter their student ID number: ')
    return get_student_id_loaned_books(student_id)


# def librarian_adds_a_book():
#     print('Please enter what books you\'d like to add to the library')
#     enterBook = input('Please enter the title, author, year published, subject, description')
#     add_new_book(enterBook)


if __name__ == '__main__':
    welcome_to_library()
    # run_student_id_loaned_books()
    # run_get_all_books()
    # run_view_all_students()

