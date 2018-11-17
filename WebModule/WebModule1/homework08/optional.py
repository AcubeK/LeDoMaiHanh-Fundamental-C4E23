from flask import Flask, render_template

app = Flask(__name__)

@app.route("/user/<username>")
def user(username):
    usernames = {
        "A" : {
            "Name": "Bucko",
            "Age": "None",
            "Bio": "A Deity"
            },
        "B" : {
            "Name": "Robert",
            "Age": 19,
            "Bio": "A Creation"        
        },
        "C" : {
            "Name": "William",
            "Age": 23,
            "Bio": "A Creation"
        },
        "D" : {
            "Name": "Jule",
            "Age": 16,
            "Bio": "An user"
        },
        "E": {
            "Name": "Gilbert",
            "Age": 30,
            "Bio": "An AI"
        },
        "F": {
            "Name": "Ashleigh",
            "Age": 27,
            "Bio": "A Malfunction"
        }
    }
    if username in usernames:
        u = usernames[username]
        return render_template("optional.html", user = u)
    else:
        return "User not found"
if __name__ == "__main__":
    app.run()