#TODO: Exercise 5: Data extraction for the first product
# 1. Use 'ProductRequest' to create a new request
# 2. Assign the result of .get() method execution to a new variable called 'res'
# 3. Create a new variable 'res_data: Dict = res.json()'
# 4. Get the first product from the 'results' key in 'res_data'
#    and assign it to a new variable called 'product'
# 5. Find out how to access product fields:
#    'title', 'image', 'full_link', 'current_price', 'currency'
#    using 'product' variable
# 6. Create a new empty 'List' variable called 'products'
# 7. Append a new item
#    (Dict with product 'title', 'image', 'full_link', 'current_price', 'currency')
#    to 'products'

import requests
from typing import Dict, List


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
data: Dict = {
    'country': 'US',
    'query': 'Hair+product'
}

res: requests.Response = requests.get(
    params=data,
    url='https://amazon-products1.p.rapidapi.com/search'
)

res_data: Dict = res.json()


print(res.json())

# product: str = res.json()['results'][0].get('title')
# image: str = res.json()['results'][0].get('image')
# full_link: str = res.json()['results'][0].get('full_link')
# current_price: Dict = res.json()['results'][0].get('current_price')
# currency: Dict = res.json()['results'][0].get('currency')
#
# products: List = []



# products.append(
#     product, image, full_link, current_price, currency,
# )

# print(res.json()['results'][0].get('title'))
# print(res.json()['results'][0].get('image'))
# print(res.json()['results'][0].get('full_link'))
# print(res.json()['results'][0].get('current_price'))
# print(res.json()['results'][0].get('currency'))







