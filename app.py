from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home_page():
    return "<h4> Homework №15. Aleksey Kubarev</h4>"


@app.route("/hello_world")
def hello_world():
    return "Hello world!"


@app.route("/<name>/<int:number>")
def dynamic_route(name, number):
    return f"Hello {name}! Your number is {number}."


# http://127.0.0.1:5000/greeting?name=Thomas&number=27
@app.route("/greeting")
def query_route():
    name = request.args.get("name")
    number = request.args.get("number")

    return f"Hello {name}! Your number is {number}."


if __name__ == "__main__":
    app.run()
