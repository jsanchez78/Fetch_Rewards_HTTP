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

