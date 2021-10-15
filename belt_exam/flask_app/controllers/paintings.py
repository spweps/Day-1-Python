from flask_app import app
from flask import render_template,request,flash,redirect,session
from flask_app.models.painting import Painting


@app.route("/add/painting",methods=["POST"])
def add_painting():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template("painting_add.html",user=User.get_by_id(data)


# @app.route
#     if Painting.validate_painting(request.form):
#         data = {
#         "artist":request.form["artist"],
#         "title":request.form["title"],
#         "price":request.form["price"]
#         }
#         Painting.add_painting(data)
#     return redirect("/dashboard")



@app.route('/edit/painting', methods=["POST"])
def edit_painting(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("painting_edit.html",edit=painting.get_one(data),user=User.get_by_id(user_data))



@app.route("/delete/<int:id>")
def delete(id):
    if "user_id" not in session:
        flash("Must be logged in to view page")
        return redirect("/")
        
    data = {            
        "id":id
    }
    Painting.delete_painting(data)
    return redirect("/dashboard")