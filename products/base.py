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
        "country":"US","query":"Dandruff"
    }
)

data_product = response.json()

# print(data)
# print(response.json()["results"][0].get('title'))
# print(response.json()["results"][0].get('image'))
# print(response.json()["results"][0].get('full_link'))
# print(response.json()["results"][0].get('prices'))

# "Dandruff" - 60
# "Hair loss" - 60
# "Dry hair" - 48
# "Psoriasis" - 60
# "Head lice" - 60
# "Bamboo hair" - 60
# "Very oily hair" - 48

#TODO: Exercise 2: Create a 'ProductRequest' class
# 1. Create a new 'ProductRequest' class blueprint
# 2. Create a new method called 'def _request(self) -> requests.Response:'
# 3. Move the content of 'Exercise 1' to the new '_request' method (return the response)

#TODO: Exercise 3: Move parts that don't change to the __init__
# 1. Create a new 'self.url' variable in '__init__' method (and use it in code)
# 2. Create a new 'self.headers' variable in '__init__' method (and use it in code)

#TODO: Exercise 4: Add 'timeout' (in case we can't reach the API url)
# 1. Create a separate method called '.get()' in 'ProductRequest' class
# 2. Adjust '_request' method to use 'getattr()' and '**kwargs' (see the video)
# 3. Add new variable called 'self.timeout' to __init__ method (see the video)
# 4. Update 'kwargs' with 'self.timeout' in '_request' method (see the video)
# 5. Adjust '.get()' method to use '_request' method (see the video)

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
    'query': 'Hair+product'
}

request = ProductRequest()
res: requests.Response = requests.get(
    params=data,
    url='https://amazon-products1.p.rapidapi.com/search'
)
from typing import List
# print(res.json())

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

res_file: requests.Response = request.get(params=data)
res_data: Dict = res.json()


# product: str = res_file.json()['results'][0].get('title')
# image: str = res_file.json()['results'][0].get('image')
# full_link: str = res_file.json()['results'][0].get('full_link')
# current_price: Dict = res_file.json()['results'][0].get('current_price')
# currency: Dict = res_file.json()['results'][0].get('currency')


# print(res_file.json()['results'][0].get('title'))
# print(res_file.json()['results'][0].get('image'))
# print(res_file.json()['results'][0].get('full_link'))
# print(res_file.json()['results'][0].get('current_price'))
# print(res_file.json()['results'][0].get('currency'))

products: List = []

# products.append(
#     [
#         product,
#         image,
#         full_link,
#         current_price,
#         currency,
#     ]
# )

# print(products)


#TODO: Exercise 6: Create 'get_products' function
# 1. Create a new function called 'get_products'
# 2. 'get_products' function takes 1 argument 'res_data'
# 3. The goal of the function is to return a list of 5 products
# 4. Each product should be appended to the 'products' list
#    as a Dict with with product 'title', 'image', 'full_link', 'current_price', 'currency'
# 5. Use 'for loop' to with 'break' statement to end the 'for loop' once you have collected 5 products
# 6. Use if statement to only add products with current_price higher than -1.0 (float)
# 7. The function should return a list of products (add a return type to the function)

def get_products(res_data):

    products: List = []

    for res_file.json()['results'] in res_data:
        return products.append(x)

