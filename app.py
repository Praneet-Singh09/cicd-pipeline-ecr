from flask import Flask, jsonify

app = Flask(__name__)


def add(a, b):
    return a + b


@app.route("/")
def home():
    return jsonify({
        "message": "CI/CD Pipeline Demo",
        "status": "Application is running"
    })


@app.route("/add/<int:a>/<int:b>")
def add_numbers(a, b):
    return jsonify({"result": add(a, b)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
