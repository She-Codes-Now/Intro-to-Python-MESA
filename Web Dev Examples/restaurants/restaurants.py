from flask import Flask, render_template, request, url_for, redirect
from restaurants_model import RestaurantModel, BaseModel
from sqlalchemy import create_engine

import os

app = Flask(__name__)


@app.before_first_request
def create_all():
    # create only once
    if not os.path.exists('restaurant.db'):
        engine = create_engine('sqlite:///restaurant.db')
        BaseModel.metadata.create_all(engine)


@app.route('/restaurants', methods=['GET'])
@app.route('/', methods=['GET'])
def restaurantsList():
    restaurants = RestaurantModel.get_all()
    return render_template("restaurantsList.html", restaurants=restaurants)


@app.route('/restaurant/add', methods=['GET', 'POST'])
def create_restaurant():
    if request.method == "GET":
        return render_template("addRestaurant.html")
    else:
        nm = request.form['rname']
        loc = request.form['rloc']
        new_restaurant = RestaurantModel(name=nm, location=loc)
        new_restaurant.save_to_db()
        return redirect(url_for('restaurantsList'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
