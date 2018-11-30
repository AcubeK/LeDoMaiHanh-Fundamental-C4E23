from flask import Flask, render_template, request
import mlab
from movie import Movie
from register import Register
from gmail import GMail, Message

mlab.connect()

gmail = GMail("akbaacs@gmail.com", "AK0489x6")

app = Flask(__name__)

# @app.route("/add_movie", methods = ["GET", "POST"] )
# def add_movie():
#     if request.method =="GET":
#         #User request form
#         return render_template("add_movie.html")
#     elif request.method == "POST":
#         form = request.form
#         t = form["title"]
#         img = form["image"]
#         y = form["year"]
#         m = Movie(title =t, image = img, year = y)
#         m.save()
#         return "Gotcha"

@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        form = request.form
        username = form["username"]
        password = form["password"]
        email = form["email"]

        # user_list = Register.objects()
        # for u in user_list:
        #     if username == u.username:
        #         return "Username is already taken."
        #     elif email == u.email:
        #         return "Email is already taken."
        
        u = Register.objects(username = username).first()
        if u != None:
            return "Username taken."
        
        e = Register.objects(email = email).first()
        if e != None:
            return "Email taken"

        r = Register(username =username, password = password, email = email)
        r.save()
        message = Message("Confirm", to = email, text = "Success")
        gmail.send(message)
        return "Success"


if __name__ == "__main__":
    app.run(debug = True)
