from flask import Flask, send_file, jsonify


app = Flask(__name__)


@app.route('/sort', methods=["POST"])
def sort():
    # Implement the sort algoritm right here
    return jsonify([1, 2, 3, 4])


@app.route('/')
def index():
    return send_file("index.html")


if __name__ == "__main__":
    print("Starting server at http://localhost:7357")
