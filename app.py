from flask import Flask, jsonify,request
from db_utils import *

app=Flask(__name__)

@app.route('/books',methods=['GET'])

def  get_book():
    data={"Books":RunQuery()}
    return jsonify(data),200

if __name__=='__main__':
    app.run(debug=True)