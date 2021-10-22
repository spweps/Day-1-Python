from flask_app import app
from flask import render_template,request,flash,redirect,session
from flask_app.models.show import Show
from flask_app.models.user import User


@app.route("/add/show")
def add_show():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template("add_show.html",user=User.get_by_id(data))


@app.route("/create/show", methods=["POST"])
def create_show():
    if Show.validate_show(request.form):
        data = {

        "id":session["user_id"],
        "title":request.form["title"],
        "release_date":request.form["release_date"],
        "description":request.form["description"],
        "network":request.form["network"],
        
        }
        Show.add_show(data)
    return redirect("/dashboard")


@app.route('/edit/show/<int:id>')
def edit_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_show.html",show=Show.get_one(data),user=User.get_by_id(user_data))

@app.route('/edit/show/<int:id>', methods=["POST"])
def update_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id,
        "title":request.form["title"],
        "release_date":request.form["release_date"],
        "description":request.form["description"],
        "network":request.form["network"],
    }
    print(data)
    user_data = {
        "id":session['user_id']
    }
    Show.update_show(data)
    return redirect("/dashboard")


@app.route("/delete/<int:id>")
def delete(id):
    if "user_id" not in session:
        flash("Must be logged in to view page")
        return redirect("/")
        
    data = {            
        "id":id
    }
    Show.delete_show(data)
    return redirect("/dashboard")

@app.route("/show/<int:id>")
def show_show(id):
    data={
        "id":id
    }
    show = Show.get_one(data)
    return render_template("show_show.html", show=show)

@app.route('/destroy/show/<int:id>')
def destroy_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Show.destroy(data)
    return redirect('/dashboard')
