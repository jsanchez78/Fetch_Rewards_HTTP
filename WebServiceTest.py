import json
import unittest

import pytest as pytest
from flask import Flask

import app


class WebServiceTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def app_context(self):
        a = Flask(__name__)
        with a.app_context():
            yield

    def test_initial_balance(self):
        initial_balance = open('balances.json')
        # returns JSON object as
        # a dictionary
        data = json.load(initial_balance)
        self.assertEqual(app.balance().json, data)

    def test_spend(self):
        initial_balance = open('spend.json')
        data = json.load(initial_balance)
        self.assertEqual(app.spend_points().json, data)


if __name__ == '__main__':
    unittest.main()
