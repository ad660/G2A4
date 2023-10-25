from flask import Flask, jsonify, request
from db_utils import (get_all_students, get_all_books, get_books_by_student_id,
                      add_new_book, add_student, delete_graduated_students)

app = Flask(__name__)
app.json.sort_keys = False

@app.route('/books', methods=['GET'])
def get_book():
    data = {"Books": get_all_books()}
    return jsonify(data), 200


@app.route('/books_on_loan/<student_id>')
def get_loan_books_for_student(student_id):
    student_loaned_books = get_books_by_student_id(student_id)
    app.json.sort_keys = False
    return jsonify(student_loaned_books), 200
# e.g. http://127.0.0.1:5001/books_on_loan/10


@app.route('/add_book', methods=['POST'])
def add_book():
    if request.method == 'POST':
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        year_published = data.get('year_published')
        subject = data.get('subject')
        description = data.get('description')
        age_restrict = data.get('age_restrict')
        stockID = data.get('stockID')

        add_new_book(title, author, year_published, subject, description, age_restrict, stockID)

        return jsonify({"message": "Book added successfully"}), 200

# To test it follow these steps:

# 1. Open Insomnia:
#    Launch the Insomnia application on your computer.

# 2. Create a New Request:
#    Click the '+ New Request' button in the top-left corner to create a new request.

# 3. Set Method to POST:
#    In the newly created request, select "POST" as the method from the dropdown menu next to the URL bar.

# 4. Enter the URL:
#    In the URL bar, enter the full address of your Flask application. In your case, it will be http://localhost:5000/add_book.

# 5. Add Content-Type Header:
#    In the headers section, add the Content-Type header and set its value to application/json.

# 6. Enter JSON Data:
#    Go to the section where you can enter data to be sent as JSON. Enter the data in JSON format, for example:

#    ```json
#    {
#        "title": "New Book",
#        "author": "New Author",
#        "year_published": 2023,
#        "subject": "New Subject",
#        "description": "New Description",
#        "age_restrict": "For All",
#        "stockID": "new_stockID"
#    }
#    ```

# 7. Send the Request:
#    Click the 'Send' button (or use the shortcut Ctrl + Enter or Cmd + Enter on Mac) to send the POST request to your Flask application.

# 8. Read the Response:
#    Insomnia should display the response from your application. If everything is fine, you should see the message "Book added successfully".

# Note: Make sure your Flask application is running (e.g., `python app.py`) while testing with Insomnia.
#       Additionally, ensure that your Flask routes are correctly defined in `app.py`.


@app.route('/add_student', methods=['PUT'])
def update_student():
    if request.method == 'PUT':
        data = request.get_json()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        birth_date = data.get('birth_date')
        house = data.get('house')
        email = data.get('email')
        join_date = data.get('join_date')

        add_student(first_name, last_name, birth_date, house, email, join_date)

        return jsonify({"message": "Student added successfully"}), 200


@app.route('/students', methods=['GET'])
def get_students():
    delete_graduated_students()
    students_data = {"Students": get_all_students()}
    return jsonify(students_data), 200


if __name__ == '__main__':
    app.run(debug=True)
