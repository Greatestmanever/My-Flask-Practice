from flask import Flask, render_template

app = Flask(__name__)


@app.route("/for-loop/conditionals/")
def render_for_loop_conditionals():
    user_os= {
        "King Greatman Justus":  "MacOS" ,
        "Rex Zoe Favour Ambali":  "Linux" ,
        "Greatness Undefined":  "UNIX" ,
        "Chike Sarima Esther":  "Windows" ,
    }

    return render_template("loops_and_conditionals.html", user_os=user_os)