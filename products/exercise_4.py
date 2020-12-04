# TODO: Exercise 4: Add 'timeout' (in case we can't reach the API url)
# 1. Create a separate method called '.get()' in 'ProductRequest' class
# 2. Adjust '_request' method to use 'getattr()' and '**kwargs' (see the video)
# 3. Add new variable called 'self.timeout' to __init__ method (see the video)
# 4. Update 'kwargs' with 'self.timeout' in '_request' method (see the video)
# 5. Adjust '.get()' method to use '_request' method (see the video)


import requests
from typing import Dict


class ProductRequest:

    def __init__(self):
        self.url = "https://amazon-products1.p.rapidapi.com/search"
        self.headers = {
            'x-rapidapi-key':
                "a8f0a072d2msh3d1bfc104318241p1aec10jsn70718bbf81a2",
            'x-rapidapi-host':
                "amazon-products1.p.rapidapi.com"
        }
        self.timeout = 20

    def _request(self, method: str, **kwargs) -> requests.Response:
        kwargs.update({
            'timeout': self.timeout
        })
        return getattr(requests, method)(**kwargs)

    def get(self, params: Dict) -> requests.Response:
        return self._request(
            method='get',
            url=self.url,
            headers=self.headers,
            params=params,
        )
