from flask import Flask, jsonify, request
from db_utils import get_all_books, add_new_book, get_books_by_student_id, get_all_students

app = Flask(__name__)


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


@app.route('/students', methods=['GET'])
def get_students():
    data = {"Students": get_all_students()}
    return jsonify(data), 200

#
# @app.route('/students/delete_graduated, methods=['DELETE'])
# def delete_graduated_students():
#     if request.method == 'DELETE':
#         data = request.get_json()
#         title = data.get('title')
#         author = data.get('author')
#         year_published = data.get('year_published')
#         subject = data.get('subject')
#         description = data.get('description')
#         age_restrict = data.get('age_restrict')
#         stockID = data.get('stockID')
#
#         return jsonify({"message": "Students deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
