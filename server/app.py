#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakeries = []
    for bakery in Bakery.query.all():
        bakery_dict = bakery.to_dict()
        bakeries.append(bakery_dict)

    response = make_response(
        jsonify(bakeries),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery =  Bakery.query.filter_by(id=id).first()
    bakery_dict = bakery.to_dict()

    response = make_response(
        jsonify(bakery_dict),
        200
    )
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    goods=[]
    goods_by_price = BakedGood.query.order_by(BakedGood.price).all()
    for good in goods_by_price:
        good_dict = good.to_dict()
        goods.append(good_dict)
    
    response = make_response(
        jsonify(goods),
        200
    )
    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    most_expensive_good = BakedGood.query.order_by(BakedGood.price).first()
    good_dict = most_expensive_good.to_dict()

    response = make_response(
        jsonify(good_dict),
        200
    )
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
