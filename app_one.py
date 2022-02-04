# from flask import Flask, render_template
# from flask.templating import render_template_string

# app = Flask(__name__)

# @app.route("/jinja")
# def hello_world():
#     return render_template (
#         "jinja_intro.html", name="King Greatman Justus", template_name="Jinja2", template_one="Django"
#         )

# app = Flask(__name__)

# @app.route("/expressions/")
# def hello_world():

#     # Interpolation
#     color = "brown"
#     animal_one = "fox"
#     animal_two = "dog"

#     # Addition and Subtraction
#     banana_amount = 11
#     mango_amount = 15
#     donate_amount = 13

#     # String Concatenation
#     first_name = "John"
#     last_name = "The Divine"

#     kwargs = {
#         "color": color,
#         "animal_one": animal_one,
#         "animal_two":animal_two,
#         "banana_amount":banana_amount,
#         "mango_amount": mango_amount,
#         "donate_amount": donate_amount,
#         "first_name": first_name,
#         "last_name": last_name,
#     }

#     return render_template(
#         "expressions.html", **kwargs
#     )

from flask import Flask, render_template

app = Flask(__name__)

class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

@app.route("/data-structures/")
def render_data_structures():

    movies = [
        "Avengers - The End Game",
        "The Boy's Choir",
        "The Passion of Christ"
    ]

    car = {
        "year": "2020",
        "brand": "Mercedez",
        "model": "Benz",
    }

    moons = GalileanMoons("To", "Europe", "Gamymede", "Callisto")

    kwargs = {
        "movies":movies,
        "car": car,
        "moons": moons
    }
    return render_template("data_structures.html", **kwargs)

# conditional basics
    from flask import Flask, render_template

app = Flask(__name__)

@app.route("/conditionals-basics/")
def render_data_structures():
    company = "Apple"
    return render_template("conditionals_basics.html", company=company)

    #for loops
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/for-loop/")
def render_loops_for():
    months_in_a_year = [
        "January",
        "Febuary",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    return render_template("for_loop.html", months_in_a_year=months_in_a_year)
