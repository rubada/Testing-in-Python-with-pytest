import os
import requests


def remove_file(filename):
    os.remove(filename)


def create_file(filename, data):
    with open(filename, "w") as file:
        file.write(data)


def get_user_data(user_id):
    response = requests.get(f"https://api.userdata.com/{user_id}")
    return response.json()


class APIClient:

    def get_data(self, user_id):
        response = requests.get(f"https://api.userdata.com/{user_id}")
        return response.json()
        # pass


def fetch_from_cache(cache, key):
    # Simulates fetching a value from cache
    try:
        return cache[key]
    except ValueError as e:
        return f"Error: {e}"
