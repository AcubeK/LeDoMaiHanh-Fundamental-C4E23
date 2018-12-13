from flask import Flask, render_template, request, redirect, session, url_for
import mlab
from models.activities import Activities
from models.information import Information
from models.attribute import Attribute
from models.habit import Habit
from urllib.request import urlopen

mlab.connect()

app = Flask(__name__)
app.config["SECRET_KEY"] = "qazqwsxcedcyhntyu"


@app.route("/sign_up", methods=["GET","POST"])
def sign_up():
    if request.method == "GET":
        return render_template("sign_up.html")
    else: 
        form = request.form 
        username = form["username"]
        email = form["email"]
        fullname = form["fullname"]
        password = form["password"]
        confirm = form["confirm"]
        if username == "" or email == "" or fullname == "" or password == "" or confirm == "":
            return "You must complete the information"
        if len(username) < 8:
            return render_template("sign_up_eror.html")
        if "@" not in email:
            return "Email is not available"
        if len(password) < 8:
            return "Password is not available"
        if confirm == password:
            m = Information(username= username, email= email, fullname= fullname, password= password)
            m.save()  #Save
            return redirect("/sign_in")     
        else:
            return "Sorry! Wrong password authentication"


@app.route("/sign_in",methods=["GET","POST"])
def sign_in():
    if request.method == "GET":
        return render_template("sign_in.html")
    else:
        form = request.form 
        username = form["username"]
        password = form["password"] 
        found_user = Information.objects(username= username).first()
        if found_user is None:
            return "Sorry! User does not exist"
        elif found_user.password != password:
            return "Sorry! Wrong password"
        else:
            session["token"] = username
            return redirect(url_for("home"))


@app.route("/logout")
def log_out():
    if "token" in session:
        del session["token"]
    return redirect(url_for("login"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ca-nhan")
def ca_nhan():
    if "token" in session:
        user = session["token"]
        info = Information.objects(username = user).first()
        att = Attribute.objects(username = user).first()
        return render_template("ca_nhan.html", info = info, att = att)
    else:
        return "Khong phai nguoi dung"

@app.route("/hoat-dong", methods = ["GET","POST"])
def hoat_dong():
    if request.method == "GET":
        act_list = Activities.objects()
        return render_template("hoat_dong.html", act = act_list)
    else:
        if "token" in session:
            user = session["token"]
            form = request.form
            act_list = Activities.objects()
            att_list = Attribute.objects(username = user).first()
            for act in act_list:
                action = form.get(act["tit"])
                if action != None:
                    for att in att_list :
                        if att in act and att != "id":
                            att_list[att] = att_list[att] + act[att]
                            if att_list[att] < 0:
                                att_list[att] = 0 
                    att_list.save()
                    break                   
            return render_template("hoat_dong.html", act = act_list)
        else:
            return "Dang nhap de co the su dung."
# for a in act:
#     if a["tit"] == action:
#         print("Ok")

    
if __name__ == '__main__':
  app.run(debug=True)