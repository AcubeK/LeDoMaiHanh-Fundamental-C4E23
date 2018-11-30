from flask import Flask, render_template, request
from bike import Bike
import mlab

mlab.connect()

app = Flask(__name__)

@app.route("/new-bike", methods = ["GET", "POST"])
def bike_rental():
    if request.method == "GET":
        return render_template("bikes.html")
    else:
        form = request.form
        model = form["model"]
        dfee = form["dfee"]
        img = form["img"]
        year = form["year"]

        print(model, dfee, img, year, sep = "\n")

        u = Bike.objects(model = model).first()
        if u != None:
            return "Model already submitted."

        b = Bike(model = model, daily_fee= dfee, image = img, year = year)
        b.save()
    return "Succeed"
if __name__ == "__main__":
    app.run(debug=True)