from app import app
from modules.calculator import *

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/add/<number_1>/<number_2>")
def add_in_browser(number_1, number_2):
    return f"The answer is {add(int(number_1), int(number_2))}"

@app.route("/subtract/<number_1>/<number_2>")
def subtract_in_browser(number_1, number_2):
    return f"The answer is {subtract(int(number_1), int(number_2))}"

@app.route("/multiply/<number_1>/<number_2>")
def multiply_in_browser(number_1, number_2):
    return f"The answer is {multiply(int(number_1), int(number_2))}"

@app.route("/subtract/<number_1>/<number_2>")
def divide_in_browser(number_1, number_2):
    return f"The answer is {divide(int(number_1), int(number_2))}"