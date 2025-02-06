import os
from flask import Flask, json, render_template, request


def save_orders(orders, filename):
    with open(filename, "w") as f:
        # Исправлено: используем переменную `orders` вместо `order`
        json.dump(orders, f, indent=2)
    return "Заказ сохранен"


def load_orders(filename):
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, "r") as f:
            try:
                orders = json.load(f)
            except json.JSONDecodeError:
                # Если файл содержит некорректный JSON, возвращаем пустой список
                orders = []
    else:
        orders = []
    return orders


orders = load_orders("orders.json")

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title="Главная страница")


@app.route("/order", methods=("GET", "POST"))
def order():
    if request.method == "POST":
        new_order = {
            "name": request.form["name"],
            "drink": request.form["drink"],
            "dishes": request.form.getlist("dishes"),
            "garnishes": request.form.getlist("garnishes"),
        }
        orders.append(new_order)
        save_orders(orders, "orders.json")
        return render_template(
            "print.html", new_order=new_order, title="Инфо о вашем заказе"
        )
    return render_template("forms.html", title="Страница заказа")


if __name__ == "__main__":
    app.run(debug=True)
