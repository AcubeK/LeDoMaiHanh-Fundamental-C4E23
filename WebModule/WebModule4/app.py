from flask import Flask, render_template, request, session, redirect,url_for
import mlab
from models.movies import Movie
from models.users import User

mlab.connect()

app = Flask(__name__)
app.config["SECRET_KEY"] = "asbacin3oj5oi45;ll1"


@app.route("/profile")
def profile():
    if "token" in session:
        username = session["token"]
        user = User.objects(username = username).first()
        movies = Movie.objects(user = user)

        return render_template("profile.html", movie_list = movies)
    else:
        return "Access denied."

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        form = request.form
        usrnm = form["username"]
        pswrd = form["password"]
        
        u = User.objects(username = usrnm).first()
        if u == None:
            return "Username not available."
        else:
            if pswrd == u.password:
                session["token"] = usrnm
                return "User logging in."
            else:
                return "Incorrect password."
        
@app.route("/logout")
def logout():
    del session["token"]
    return redirect(url_for("login"))

@app.route("/add_movie", methods = ["GET", "POST"])
def add_movie():
    if "token" not in session:
        return redirect("/login")
    elif request.method == "GET":
        return render_template("add_movie.html")
    elif request.method == "POST":
        form = request.form
        title = form["title"]
        image = form["image"]
        year = form["year"]
        username = session["token"]
        user = User.objects(username = username).first()
        new_movie = Movie(title = title, image = image, year = year, user = user)
        new_movie.save()
        return "Added."

if __name__ == '__main__':
  app.run(debug=True)