from flask import Flask 

app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight, height):
    h = height/100
    bmi = weight/h/h
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
        
    return 'Your BMI is {} <br/> {}'.format(str("%.2f" % bmi), ans)
    
if __name__ == "__main__":
    app.run()
