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
    print("If you would like to see all the books available please now select option 1: ")
    select_option = int(input("Please choose your option now: "))
    if select_option == 1:
        print("You have chosen to see all books available")
        return get_all_books()
    elif select_option == 2:
        print('There are multiple students with books on loan, their student ID\'s are: 6, 10, 12')
        student_id = int(input("To check out what books a student currently have on loan please "
                               "enter the number of their student ID : "))
        run_student_id_loaned_books(student_id)
    elif select_option is None or isinstance(select_option, (int, float)):
        print("Invalid option please enter option again ")


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


def get_all_books():
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
    # welcome_to_library()
    # run_student_id_loaned_books()
    get_all_books()

