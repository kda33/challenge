from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response(jsonify({'message': 'Internal Server Error'}))
    response.status_code = 500
    return response

if __name__ == '__main__':
    app.run()