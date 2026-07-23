from flask import Flask, render_template, request, redirect, url_for
from Model import *

app = Flask(__name__)
@app.route("/")
def restaurant():
    return render_template("restaurant.html")

@app.route("/index")
def index():
    return render_template("index.html")




@app.route("/cooks")
def cooks():
    all_cooks = Cook.select()
    return render_template("cooks.html", cooks=all_cooks)


@app.route("/cook/create", methods=["GET", "POST"])
def create_cook():

    if request.method == "POST":

        Cook.create(
            cook_name=request.form["name"],
            cook_family=request.form["family"]
        )

        return redirect(url_for("cooks"))

    return render_template("create_cook.html")


@app.route("/cook/update/<int:id>", methods=["GET", "POST"])
def update_cook(id):

    cook = Cook.get_by_id(id)

    if request.method == "POST":

        cook.cook_name = request.form["name"]
        cook.cook_family = request.form["family"]

        cook.save()

        return redirect(url_for("cooks"))

    return render_template(
        "update_cook.html",
        cook=cook
    )


@app.route("/cook/delete/<int:id>")
def delete_cook(id):

    cook = Cook.get_by_id(id)
    cook.delete_instance()

    return redirect(url_for("cooks"))
@app.route("/cook/search", methods=["GET", "POST"])
def search_cook():

    cook = None

    if request.method == "POST":

        cook_id = request.form["id"]

        cook = Cook.get_or_none(
            Cook.id == cook_id
        )

    return render_template(
        "search_cook.html",
        cook=cook
    )
@app.route("/")
def home():
    return render_template("restaurant.html")
@app.route("/customers")
def customers():

    all_customers = Customer.select()

    return render_template(
        "customers.html",
        customers=all_customers
    )


@app.route("/customer/create", methods=["GET", "POST"])
def create_customer():

    if request.method == "POST":

        Customer.create(
            customer_name=request.form["name"],
            customer_family=request.form["family"]
        )

        return redirect(url_for("customers"))

    return render_template("create_customer.html")


@app.route("/customer/update/<int:id>", methods=["GET", "POST"])
def update_customer(id):

    customer = Customer.get_by_id(id)

    if request.method == "POST":

        customer.customer_name = request.form["name"]
        customer.customer_family = request.form["family"]

        customer.save()

        return redirect(url_for("customers"))

    return render_template(
        "update_customer.html",
        customer=customer
    )


@app.route("/customer/delete/<int:id>")
def delete_customer(id):

    customer = Customer.get_by_id(id)

    customer.delete_instance()

    return redirect(url_for("customers"))
@app.route("/customer/search", methods=["GET", "POST"])
def search_customer():

    customer = None

    if request.method == "POST":

        customer_id = request.form["id"]

        customer = Customer.get_or_none(
            Customer.id == customer_id
        )

    return render_template(
        "search_customer.html",
        customer=customer
    )
@app.route("/foods")
def foods():

    all_foods = Food.select()

    return render_template(
        "foods.html",
        foods=all_foods
    )
@app.route("/food/create", methods=["GET", "POST"])
def create_food():

    if request.method == "POST":

        Food.create(
            food_name=request.form["name"]
        )

        return redirect(url_for("foods"))

    return render_template(
        "create_food.html"
    )
@app.route("/food/update/<int:id>", methods=["GET", "POST"])
def update_food(id):

    food = Food.get_by_id(id)

    if request.method == "POST":

        food.food_name = request.form["name"]

        food.save()

        return redirect(url_for("foods"))

    return render_template(
        "update_food.html",
        food=food
    )
@app.route("/food/delete/<int:id>")
def delete_food(id):

    food = Food.get_by_id(id)

    food.delete_instance()

    return redirect(url_for("foods"))

@app.route("/food/search", methods=["GET", "POST"])
def search_food():

    food = None

    if request.method == "POST":

        food_id = request.form["id"]

        food = Food.get_or_none(
            Food.id == food_id
        )

    return render_template(
        "search_food.html",
        food=food
    )
@app.route("/orders")
def orders():

    all_orders = Order.select()

    return render_template(
        "orders.html",
        orders=all_orders
    )
@app.route("/order/create", methods=["GET", "POST"])
def create_order():

    if request.method == "POST":

        customer = Customer.get_by_id(
            request.form["customer_id"]
        )

        food = Food.get_by_id(
            request.form["food_id"]
        )

        Order.create(
            customer=customer,
            food=food
        )

        return redirect(
            url_for("orders")
        )

    customers = Customer.select()
    foods = Food.select()

    return render_template(
        "create_order.html",
        customers=customers,
        foods=foods
    )
@app.route("/order/delete/<int:id>")
def delete_order(id):

    order = Order.get_by_id(id)

    order.delete_instance()

    return redirect(
        url_for("orders")
    )
@app.route("/order/search", methods=["GET", "POST"])
def search_order():

    order = None

    if request.method == "POST":

        order = Order.get_or_none(
            Order.id == request.form["id"]
        )

    return render_template(
        "search_order.html",
        order=order
    )
@app.route("/chefs")
def chefs():

    all_chefs = Chef.select()

    return render_template(
        "chefs.html",
        chefs=all_chefs
    )
@app.route("/chef/create", methods=["GET", "POST"])
def create_chef():

    if request.method == "POST":

        Chef.create(
            chef_name=request.form["name"],
            chef_family=request.form["family"]
        )

        return redirect(url_for("chefs"))

    return render_template("create_chef.html")
@app.route("/chef/update/<int:id>", methods=["GET", "POST"])
def update_chef(id):

    chef = Chef.get_by_id(id)

    if request.method == "POST":

        chef.chef_name = request.form["name"]
        chef.chef_family = request.form["family"]

        chef.save()

        return redirect(url_for("chefs"))

    return render_template(
        "update_chef.html",
        chef=chef
    )
@app.route("/chef/delete/<int:id>")
def delete_chef(id):

    chef = Chef.get_by_id(id)
    chef.delete_instance()

    return redirect(url_for("chefs"))
@app.route("/chef/search", methods=["GET", "POST"])
def search_chef():

    chef = None

    if request.method == "POST":

        chef = Chef.get_or_none(
            Chef.id == request.form["id"]
        )

    return render_template(
        "search_chef.html",
        chef=chef
    )
@app.route("/cooking-staff")
def cooking_staff():

    all_staff = CookingStaff.select()

    return render_template(
        "cooking_staff.html",
        staff=all_staff
    )
@app.route("/cooking-staff/create", methods=["GET", "POST"])
def create_cooking_staff():

    if request.method == "POST":

        chef = Chef.get_by_id(
            request.form["chef_id"]
        )

        cook = Cook.get_by_id(
            request.form["cook_id"]
        )

        CookingStaff.create(
            chef=chef,
            cook=cook
        )

        return redirect(url_for("cooking_staff"))

    chefs = Chef.select()
    cooks = Cook.select()

    return render_template(
        "create_cooking_staff.html",
        chefs=chefs,
        cooks=cooks
    )
@app.route("/cooking-staff/delete/<int:id>")
def delete_cooking_staff(id):

    staff = CookingStaff.get_by_id(id)
    staff.delete_instance()

    return redirect(url_for("cooking_staff"))
@app.route("/cooking-staff/search", methods=["GET", "POST"])
def search_cooking_staff():

    staff = None

    if request.method == "POST":

        staff = CookingStaff.get_or_none(
            CookingStaff.id == request.form["id"]
        )

    return render_template(
        "search_cooking_staff.html",
        staff=staff
    )

if __name__ == "__main__":
    app.run(debug=True)
