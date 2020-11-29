#TODO: Exercise 1: A proper request following all the previous instructions
# 1. Add variable type to the 'response'
# 2. Instead of using separate 'url' variable,
#    move 'https://amazon-products1.p.rapidapi.com/search' in .get(url=...)
# 3. Instead of using separate 'headers' variable,
#    move {... headers_content ...} in .get(headers=...)
# 4. Instead of using separate 'querystring' variable,
#    move {... querystring_content ...} in .get(params=...)
# 5. Choose one either single or double quotes,
#    and stick with them - replace all of them with one type.

import requests

response: requests.models.Response = requests.get(
    url="https://amazon-products1.p.rapidapi.com/search",
    headers={
        'x-rapidapi-key':
            "a8f0a072d2msh3d1bfc104318241p1aec10jsn70718bbf81a2",
        'x-rapidapi-host':
            "amazon-products1.p.rapidapi.com"
    },
    params={
        "country":"US","query":"MacBook+Pro"
    }
)

# print(response.text)

#TODO: Exercise 2: Create a 'ProductRequest' class
# 1. Create a new 'ProductRequest' class blueprint
# 2. Create a new method called 'def _request(self) -> requests.Response:'
# 3. Move the content of 'Exercise 1' to the new '_request' method (return the response)

#TODO: Exercise 3: Move parts that don't change to the __init__
# 1. Create a new 'self.url' variable in '__init__' method (and use it in code)
# 2. Create a new 'self.headers' variable in '__init__' method (and use it in code)

from typing import Dict

class ProductRequest:

    def __init__(self):
        self.url = 'https://amazon-products1.p.rapidapi.com/search'
        self.headers = {
        'x-rapidapi-key':
            'a8f0a072d2msh3d1bfc104318241p1aec10jsn70718bbf81a2',
        'x-rapidapi-host':
            'amazon-products1.p.rapidapi.com'
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

data: Dict = {
    'country': 'US',
    'query': 'MacBook+Pro'
}

requests = ProductRequest()
res: requests.Response = requests.get(params=data)

print(res)


#TODO: Exercise 4: Add 'timeout' (in case we can't reach the API url)
# 1. Create a separate method called '.get()' in 'ProductRequest' class
# 2. Adjust '_request' method to use 'getattr()' and '**kwargs' (see the video)
# 3. Add new variable called 'self.timeout' to __init__ method (see the video)
# 4. Update 'kwargs' with 'self.timeout' in '_request' method (see the video)
# 5. Adjust '.get()' method to use '_request' method (see the video)
