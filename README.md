# Fetch_Rewards_HTTP
A web service that accepts HTTP requests and returns responses based on points algorithm.

# Installations
## Object Serialization and Deserialization
```
pip install -U marshmallow
```
## Flask
```
pip install Flask
```
# Object Model
```python
class User(object):
    def __init__(self, payer, points, timestamp=datetime.datetime.now()):
        self.payer = payer
        self.points = points
        self.timestamp = timestamp
```
## Serializer Schema
```python
class UserSchema(Schema):
    payer = fields.Str()
    points = fields.Int()
    timestamp = fields.DateTime()

    def make_object(self, data):
        return User(**data)
```
## Sample Data
```json
{
  "transactions": [
    {
      "payer": "DANNON",
      "points": 1000,
      "timestamp": "2020-11-02T14:00:00Z"
    },
    {
      "payer": "UNILEVER",
      "points": 200,
      "timestamp": "2020-10-31T11:00:00Z"
    },
    {
      "payer": "DANNON",
      "points": -200,
      "timestamp": "2020-10-31T15:00:00Z"
    },
    {
      "payer": "MILLER COORS",
      "points": 10000,
      "timestamp": "2020-11-01T14:00:00Z"
    },
    {
      "payer": "DANNON",
      "points": 300,
      "timestamp": "2020-10-31T10:00:00Z"
    }
  ],
  "transaction": {
    "payer": "DANNON",
    "points": 2000,
    "timestamp": "2020-12-02T14:00:00Z"
  },
  "spend": {
    "points": 5000
  }
}
```
# Routes
```python
@app.route("/", methods=["POST", "GET"])
@app.route('/add', methods=['GET'])
@app.route('/spend')
@app.route('/balance')
```
# Usage
```
git clone https://github.com/jsanchez78/Fetch_Rewards_HTTP.git
cd Fetch_Rewards_HTTP
python app.py
```
Default browser will open http://127.0.0.1:5000/

## Transactions
In your app.py, 
