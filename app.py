from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# List of cities
cities = [
    "Beijing",
    "Shanghai",
    "Guangzhou",
    "Shenzhen",
    "Chengdu",
    "Chongqing",
    "Tianjin",
    "Xi'an",
    "Hangzhou",
    "Nanjing",
    "Wuhan",
    "Changsha",
    "Qingdao",
    "Dalian",
    "Shenyang",
    "Suzhou",
    "Fuzhou",
    "Jinan",
    "Ningbo",
    "Xiamen",
]

selected_list = []


@app.route("/")
def index():
    return render_template("index.html", cities=cities)


@app.route("/select_cities", methods=["POST"])
def select_cities():
    global selected_list
    selected_list = request.form.getlist("city")
    return redirect(url_for("draw"))


@app.route("/draw", methods=["GET", "POST"])
def draw():
    if request.method == "POST" and selected_list:
        city = random.choice(selected_list)
        return render_template("result.html", city=city)
    return render_template("draw.html", selected_list=selected_list)


if __name__ == "__main__":
    app.run(debug=True)
