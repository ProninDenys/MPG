from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            conversion_type = request.form["conversion_type"]
            value = float(request.form["value"])

            if conversion_type == "mpg_to_litres":
                result = 235.214 / value  
                result = f"{result:.2f} liters/100 km"
            elif conversion_type == "litres_to_mpg":
                result = 235.214 / value 
                result = f"{result:.2f} MPG"
        except (ValueError, ZeroDivisionError):
            result = "Error: Please enter a valid value!"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
