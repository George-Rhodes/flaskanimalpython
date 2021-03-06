from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from requests.api import request
import requests
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_get(self):
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = "lion"
                p.return_value.text = "ROAR"

                response = self.client.get(url_for('animal'))
                self.assertIn(b'lion',response.data)
                self.assertIn(b'ROAR',response.data)
                self.assertEqual(response.status_code, 200)