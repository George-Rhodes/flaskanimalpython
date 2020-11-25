from flask import url_for
from flask_testing import TestCase

from application import app


class TestBase(TestCase):
    def create_app(self):
        return app


class TestAnimals(TestBase):
    def test_animal(self):
        animals = [b"dog",b"turkey",b"pig",b"cat",b"snake", b"lion", b"chicken", b"robot"]
        response = self.client.get(url_for('animal_name'))
        self.assertIn(response.data, animals)
    

    def test_noise_dog(self):
        response = self.client.post(
            url_for('animal_noise'),
            data="dog",
            follow_redirects=True
        )
        self.assertIn(b"bark", response.data)
    


    def test_noise_dog(self):
        response = self.client.post(
            url_for('animal_noise'),
            data="dog",
            follow_redirects=True
        )
        self.assertIn(b"bark", response.data)

    def test_noise_turkey(self):
        response = self.client.post(
            url_for('animal_noise'),
            data="turkey",
            follow_redirects=True
        )
        self.assertIn(b"Gobble Gobble", response.data)
    
    def test_noise_pig(self):
        response = self.client.post(
            url_for('animal_noise'),
            data="pig",
            follow_redirects=True
        )
        self.assertIn(b"oink", response.data)
    
    def test_noise_cat(self):
        response = self.client.post(
            url_for('animal_noise'),
            data="cat",
            follow_redirects=True
        )
        self.assertIn(b"meow", response.data)
    
    def test_noise_snake(self):
        response = self.client.post(
            url_for('animal_noise'),
            data="snake",
            follow_redirects=True
        )
        self.assertIn(b"sssssssssssss", response.data)
    
    def test_noise_lion(self):
        response = self.client.post(
            url_for('animal_noise'),
            data="lion",
            follow_redirects=True
        )
        self.assertIn(b"ROAR", response.data)
    
    def test_noise_chicken(self):
        response = self.client.post(
            url_for('animal_noise'),
            data="chicken",
            follow_redirects=True
        )
        self.assertIn(b"cluck cluck BWAkaaaark", response.data)
    
    
    
    def test_noise_robot(self):
        response = self.client.post(
            url_for('animal_noise'),
            data="robot",
            follow_redirects=True
        )
        self.assertIn(b"01100001 01101100 01101100 00100000 01101000 01110101 01101101 01100001 01101110 01110011 00100000 01110111 01101001 01101100 01101100 00100000 01100100 01101001 01100101", response.data)


    def test_noise_none(self):
            response = self.client.post(
                url_for('animal_noise'),
                data="none",
                follow_redirects=True
            )
            self.assertIn(b"something went wrong big man", response.data)

