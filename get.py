import requests

def get_interface():
    # Rajapinnan osoite
    url = "https://jsonplaceholder.typicode.com/posts"

    # Haetaan postit
    getposts = requests.get(url)
    data = getposts.json()

    return data