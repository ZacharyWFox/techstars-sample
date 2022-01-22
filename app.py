from flask import Flask

app = Flask(__name__)

@app.route("/hello", methods = ["GET"])
def say_hi():
    return "Hello!"

@app.route("/hello/<string:name>", methods=["GET"])
def say_hi_to(name):
    return f"Hello {name}, have a good day!"