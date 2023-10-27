from flask import Flask, jsonify, request
from db_utils import (get_all_students, get_all_books, add_new_book, get_students_ids, get_books_by_student_id, add_new_student)

app = Flask(__name__)
app.json.sort_keys = False


@app.route('/books', methods=['GET'])
def get_book():
    data = {"Books": get_all_books()}
    return jsonify(data), 200


@app.route('/studentids')
def get_student_ids_in_loaned_books():
    student_ids = get_students_ids()
    return jsonify(student_ids), 200
# http://127.0.0.1:5000/studentids


@app.route('/books_on_loan/<student_id>')
def get_loan_books_for_student(student_id):
    student_loaned_books = get_books_by_student_id(student_id)
    app.json.sort_keys = False
    return jsonify(student_loaned_books), 200
# e.g. http://127.0.0.1:5001/books_on_loan/10


@app.route('/add_new_book', methods=['POST'])
def add_new_book_to_db():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    year_published = data.get('year_published')
    subject = data.get('_subject')
    description = data.get('_description')
    age_restrict = data.get('age_restrict')

    add_new_book(title, author, year_published, subject, description, age_restrict)

    return jsonify({"message": "Book added successfully"}), 200


@app.route('/add_new_student', methods=['PUT'])
def update_student():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    birth_date = data.get('birth_date')
    house = data.get('house')
    email = data.get('email')
    join_date = data.get('join_date')

    add_new_student(first_name, last_name, birth_date, house, email, join_date)

    return jsonify({"message": "Student added successfully"}), 200


@app.route('/students', methods=['GET'])
def get_students():
    # delete_graduated_students()
    students_data = {"Students": get_all_students()}
    return jsonify(students_data), 200


if __name__ == '__main__':
    app.run(debug=True)
