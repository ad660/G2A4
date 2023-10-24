from flask import Flask, jsonify, request
from db_utils import RunQuery, get_books_by_student_id

app = Flask(__name__)


@app.route('/books', methods=['GET'])
def get_book():
    data = {"Books": RunQuery()}
    return jsonify(data), 200


@app.route('/books_on_loan/<student_id>')
def get_loan_books_for_student(student_id):
    student_loaned_books = get_books_by_student_id(student_id)
    app.json.sort_keys = False
    return jsonify(student_loaned_books), 200
# e.g. http://127.0.0.1:5001/books_on_loan/10


if __name__ == '__main__':
    app.run(debug=True)
