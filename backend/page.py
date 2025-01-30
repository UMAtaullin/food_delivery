from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('./index.html')


@app.route("/order", methods=("GET", "POST"))
def order():
    if request.method == "POST":
        drink = request.form["drink"]
        print("Drink: ", drink)
        return render_template("print.html", drink=drink)
    return render_template("forms.html")


if __name__ == "__main__":
    app.run(debug=True)
