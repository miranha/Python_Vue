from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/hello', methods=['GET'])
def hello():
    print("Fromd terminal...Miran")
    return "Hello, World!"

@app.route('/value', methods=['POST'])
def receive_value():
    value = request.json['value']
    print(value)
    return value + ": From Server"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
