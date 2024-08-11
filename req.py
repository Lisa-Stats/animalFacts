import requests

def cat_request():
    cat = requests.get("https://meowfacts.herokuapp.com")
    cat_json = cat.json()
    cat_data = cat_json["data"]
    return cat_data[0]

def dog_request():
    dog = requests.get("https://dog-api.kinduff.com/api/facts")
    dog_json = dog.json()
    dog_data = dog_json["facts"]
    return dog_data[0]
