from flask import Flask, render_template 

app = Flask(__name__)

#function binding
@app.route("/")
def home():
    return "Hello Flask."

@app.route("/c4e")
def c4e():
    return "Hello C4E, ah."

@app.route("/me")
def me():
    return "Greetings."

@app.route("/hi/<name>")
def hi_minh(name):
    return name + " is so cool."

@app.route("/add/<a>/<b>")
def add(a, b):
    sum = str(int(a) + int(b))
    return sum

# @app.route("/add/<int:a>/<int:b>")
# def add(a, b):
#     sum = str(a+b)
#     return sum

@app.route("/posts/<int:a>")
def posts(a):
    title = ["Lovely inside.", "Wasn't you there few seconds?", "Ah, decide to return home?"]
    content = ["Nothing there though.", "Who.", "No way back. "*5, "Where."]
    if len(title) < len(content):
        title.append("")
    t = title[a]
    c = content[a]
    return render_template("posts.html", title = t, content = c)

@app.route("/movie")
def movie():
    return render_template("movie.html", name = "Batman", image = "https://static3.srcdn.com/wordpress/wp-content/uploads/2018/11/Batman-Justice-League-New-Comic.jpg")

@app.route("/movies")
def movies():
    # movies_titles = ["A", "B", "C", "D"]
    movie_list = [
        {"title": "A",
        "image": ""},
        {"title": "B",
        "image": ""},
        {"title": "C",
        "image": "https://static3.srcdn.com/wordpress/wp-content/uploads/2018/11/Batman-Justice-League-New-Comic.jpg"}
    ]
    return render_template("movies.html", movies = movie_list)
if __name__ == "__main__":
    app.run()

