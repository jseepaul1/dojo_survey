from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.dojo import Dojo


@app.route("/")
def index():
    return render_template("index.html", dojos=Dojo.get_all())


@app.route('/result/<int:dojo_id>')
def results(dojo_id):
    data = {
        'id': dojo_id
    }
    dojo = Dojo.get_one(data)
    return render_template("result.html", dojo=dojo)


@app.route("/create/dojo", methods=["POST"])
def create_dojo():
    if not Dojo.validate_dojo(request.form):
        return redirect("/")
    # print('form = ', request.form)
    data = {
        "name": request.form["name"],
        "dojo_location": request.form["dojo_location"],
        "favorite_language": request.form["favorite_language"],
        "comment": request.form["comment"],
    }
    dojo_id = Dojo.save(data)
    # print('dojo_id - ', dojo_id)
    return redirect(f"/result/{dojo_id}")
