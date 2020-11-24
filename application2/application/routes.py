from application import app
from flask import Response, request
import random

@app.route('/animal/name', methods=['GET'])
def animal_name():
    animal_list=["dog","turkey","pig","cat","snake", "lion", "chicken", "robot"]
    the_data = random.choice(animal_list)
    return Response(the_data, mimetype='text/plain')

@app.route('/animal/noise', methods=['POST'])
def animal_noise():
    response=request.data.decode('utf-8')
    if response == "dog":
        noise = "bark"
    elif response == "turkey":
        noise = "Gobble Gobble"
    elif response == "pig":
        noise = "oink"
    elif response == "cat":
        noise = "meow"
    elif response == "snake":
        noise = "sssssssssssss"
    elif response == "lion":
        noise = "ROAR"
    elif response == "chicken":
        noise = "cluck cluck BWAkaaaark"
    elif response == "robot":
        noise = "01100001 01101100 01101100 00100000 01101000 01110101 01101101 01100001 01101110 01110011 00100000 01110111 01101001 01101100 01101100 00100000 01100100 01101001 01100101"
    else:
        noise = "something went wrong big man"
    return Response(noise, mimetype='text/plain')