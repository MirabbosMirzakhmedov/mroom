#TODO: Exercise 3: Move parts that don't change to the __init__
# 1. Create a new 'self.url' variable in '__init__' method (and use it in code)
# 2. Create a new 'self.headers' variable in '__init__' method (and use it in code)

import requests


class ProductRequest:

    def __init__(self):
        self.url = "https://amazon-products1.p.rapidapi.com/search"
        self.headers = {
                'x-rapidapi-key':
                    "a8f0a072d2msh3d1bfc104318241p1aec10jsn70718bbf81a2",
                'x-rapidapi-host':
                    "amazon-products1.p.rapidapi.com"
            }

    def _request(self) -> requests.Response:
        response: requests.models.Response = requests.get(
            url=self.url,
            headers=self.headers,
            params={
                "country": "US", "query": "Dandruff"
            }
        )
        return response

