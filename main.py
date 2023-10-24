from flask import Flask, jsonify,request

app=Flask(__name__)


@app.route('/books', methods=['GET'])
def get_books():
    if request.method=='GET':
        data={"data":"testing"}
        return jsonify(data)
    
    if __name__ =='__main__':
        app.run(debug=True)