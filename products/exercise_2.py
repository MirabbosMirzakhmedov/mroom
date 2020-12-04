#TODO: Exercise 2: Create a 'ProductRequest' class
# 1. Create a new 'ProductRequest' class blueprint
# 2. Create a new method called 'def _request(self) -> requests.Response:'
# 3. Move the content of 'Exercise 1' to the new '_request' method (return the response)


import requests


class ProductRequest:

    def _request(self) -> requests.Response:
        response: requests.models.Response = requests.get(
            url="https://amazon-products1.p.rapidapi.com/search",
            headers={
                'x-rapidapi-key':
                    "a8f0a072d2msh3d1bfc104318241p1aec10jsn70718bbf81a2",
                'x-rapidapi-host':
                    "amazon-products1.p.rapidapi.com"
            },
            params={
                "country": "US", "query": "Dandruff"
            }
        )
        return response
