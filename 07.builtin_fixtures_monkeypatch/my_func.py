import requests


def my_string():
    return "Hello, this pytest"


def get_user_data(user_id):
    url = f"https://api.user.com/{user_id}"
    response = requests.get(url)
    return response.json()
