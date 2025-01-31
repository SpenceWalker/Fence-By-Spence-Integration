from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/home.html")
def home():
    return render_template("home.html")

@views.route("/gallery")
def gallery():
    return render_template("home.html")

@views.route("/contact.html")
def contact():
    return render_template("contact.html")

@views.route("/products.html")
def about():
    return render_template("products.html")

@views.route("/json")
def get_json():
    return jsonify({'name': 'spencer'})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def return_home():
    return redirect("views.home")