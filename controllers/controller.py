from app import app
from modules.calculator import *

@app.route("/add/<number_1>/<number_2>")
def add_in_browser(number1, number2):
    return f"The answer is {add(int(number1), int(number2))}"

@app.route("/subtract/<number1>/<number2>")
def subtract_in_browser(number1, number2):
    return f"The answer is {subtract(int(number1), int(number2))}"

@app.route("/multiply/<number1>/<number2>")
def multiply_in_browser(number1, number2):
    return f"The answer is {multiply(int(number1), int(number2))}"

@app.route("/subtract/<num1>/<num2>")
def divide_in_browser(number1, number2):
    return f"The answer is {divide(int(number1), int(number2))}"