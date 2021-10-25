import datetime
import json
from flask import Flask, redirect, url_for, render_template, request
from flask import Flask, jsonify, request
import requests as req
from marshmallow import Schema, fields, pprint

# Set Up
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
api_url = 'https://httpbin.org/post'

# Populate Data
file = open('package.json', )
data = json.load(file)
transactions = data['transactions']
t = data['transaction']
spend = data['spend']


# Model
class User(object):
    def __init__(self, payer, points, timestamp=datetime.datetime.now()):
        self.payer = payer
        self.points = points
        self.timestamp = timestamp

    def getPayer(self):
        return self.payer

    @property
    def getPoints(self):
        return self.points


# Serializer Schema
class UserSchema(Schema):
    payer = fields.Str()
    points = fields.Int()
    timestamp = fields.DateTime()

    def make_object(self, data):
        return User(**data)


if __name__ == '__main__':
    app.run()


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        usr = request.form["nm"]
        add(usr)
        return redirect(url_for("add"))
    else:
        return render_template("transactions.html")


@app.route('/add', methods=['GET'])
def addAll():
    return jsonify(transactions)


@app.route('/add', methods=['POST'])
def add(u):
    """
    Sample data
    u = {
        "payer": "DANNON",
        "points": 6000,
        "timestamp": "2020-12-02T14:00:00Z"
    }
    """
    transactions.append(json.loads(u))
    return jsonify(transactions)


@app.route('/spend_request', methods=['GET'])
def get_points():
    return jsonify(spend)


@app.route('/spend')
def spend_points():
    remaining = spend['points']
    # Rule 1: Sort by date
    transactions.sort(key=lambda s: s['timestamp'])
    response = {}
    # Spend points
    for t in transactions:
        if remaining - t['points'] > 0:
            remaining -= t['points']
            # Update existing payer
            if t['payer'] in response:
                response.update({t['payer']: response[t['payer']] - t['points']})
            else:
                response[t['payer']] = -t['points']
            # Rule 2: No payers points can go negative
        else:
            response[t['payer']] = -remaining
            break
    # Object Serialization
    schema = UserSchema(only=("payer", "points"))
    ret = []
    for k, v in response.items():
        ret.append(schema.dump(User(k, v)))
    return jsonify(ret)


@app.route('/balance')
def balance():
    # Object Deserialization
    response = spend_points().json
    schema = UserSchema(only=("payer", "points"), many=True)
    users = schema.dump(response)

    # payer -> User()
    balances = {}
    for u in users:
        balances[u['payer']] = u

    response = {}
    # Traverse transactions (cumulative points)
    for t in transactions:
        if t['payer'] in response:
            response.update({t['payer']: response[t['payer']] + t['points']})
        else:
            response[t['payer']] = t['points']
    # Update points for users
    for k, v in response.items():
        response.update({k: v + balances[k]['points']})

    return jsonify(response)
