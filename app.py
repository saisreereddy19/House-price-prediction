from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression
import joblib

model = joblib.load("housemodel.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        area = request.form["area"]
        bedrooms = request.form["bedrooms"]
        bathrooms = request.form["bathrooms"]
        stories = request.form["stories"]

        if request.form["mainroad"] == "yes" or "YES":
            mainroad = 1 
        elif request.form["mainroad"] == "no" or "NO":
            mainroad = 0

        if request.form["guestroom"] == "yes" or "YES":
            guestroom = 1 
        elif request.form["guestroom"] == "no" or "NO":
            guestroom = 0
        
        if request.form["basement"] == "yes" or "YES":
            basement = 1
        elif request.form["basement"] == "no" or "NO":
            basement = 0
        

        if request.form["airconditioning"] == "yes" or "YES":
            airconditioning = 1
        elif request.form["airconditioning"] == "no" or "NO":
            airconditioning = 0
    
        parking = request.form["parking"]

        if request.form["furnishingstatus"] == "furnished":
            furnishingstatus = 2
        elif request.form["furnishingstatus"] == "semi-furnished":
            furnishingstatus = 1
        elif request.form["furnishingstatus"] == "unfurnished":
            furnishingstatus = 0

        ans = model.predict([[float(area),float(bedrooms),float(bathrooms),float(stories),float(mainroad),float(guestroom),float(basement),float(airconditioning),float(parking),float(furnishingstatus)]])
        
        return render_template("result.html", content=round(ans[0],2))
    return render_template("index.html")

if __name__ == "__main__":
    app.run()