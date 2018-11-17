from flask import Flask, render_template

app = Flask(__name__)

@app.route("/bmi/<int:m>/<int:h>")
def bmi(m, h):
    h = h/100
    bmi = m/h/h 
    if bmi<16:
        ans = "You're severely underweight."
    elif bmi<18.5:
        ans = "You're underweight."
    elif bmi<25:
        ans = "You're normal."
    elif bmi<30:
        ans = "You're overweight."
    else:
        ans = "You're obese."
        
    return render_template("bmi.html", bmi = "%.2f" % bmi, ans = ans )
if __name__ == "__main__":
    app.run()
