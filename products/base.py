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

#TODO: Exercise 2: Create a 'ProductRequest' class
# 1. Create a new 'ProductRequest' class blueprint
# 2. Create a new method called 'def _request(self) -> requests.Response:'
# 3. Move the content of 'Exercise 1' to the new '_request' method (return the response)

#TODO: Exercise 3: Move parts that don't change to the __init__
# 1. Create a new 'self.url' variable in '__init__' method (and use it in code)
# 2. Create a new 'self.headers' variable in '__init__' method (and use it in code)

# TODO: Exercise 4: Add 'timeout' (in case we can't reach the API url)
#  1. Create a separate method called '.get()' in 'ProductRequest' class
#  2. Adjust '_request' method to use 'getattr()' and '**kwargs' (see the video)
#  3. Add new variable called 'self.timeout' to __init__ method (see the video)
#  4. Update 'kwargs' with 'self.timeout' in '_request' method (see the video)
#  5. Adjust '.get()' method to use '_request' method (see the video)

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

#TODO: Exercise 6: Create 'get_products' function
# 1. Create a new function called 'get_products'
# 2. 'get_products' function takes 1 argument 'res_data'
# 3. The goal of the function is to return a list of 5 products
# 4.
# 4. Each product should be appended to the 'products' list
#    as a Dict with with product 'title', 'image', 'full_link', 'current_price', 'currency'
# 5. Use 'for loop' to with 'break' statement to end the 'for loop' once you have collected 5 products
# 6. Use if statement to only add products with current_price higher than -1.0 (float)
# 7. The function should return a list of products (add a return type to the function)import requests
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
    'query': 'Dandruff'
}

request = ProductRequest()
res: requests.Response = request.get(
    params=data
)
res_data: Dict = res.json()

# print(res_data)

product: str = res.json()['results'][0].get('title')
image: str = res.json()['results'][0].get('image')
full_link: str = res.json()['results'][0].get('full_link')
current_price: Dict = res.json()['results'][0]['prices']['current_price']
currency: int = res.json()['results'][0]['prices']['currency']

# print(res.json()['results'][0].get('title'))
# print(res.json()['results'][0].get('image'))
# print(res.json()['results'][0].get('full_link'))
# print(res.json()['results'][0]['prices']['current_price'])
# print(res.json()['results'][0]['prices']['currency'])

products: List = []

products.append(
    {
        'product': product,
        'image': image,
        'full_link': full_link,
        'current_price': current_price,
        'currency': currency,
    }
)

# EXERCISE 6

def get_products(res_data) -> List:

    products_value: Dict = {}
    products_list: List = []

    for products[0] in res_data :
        products_value += res_data
        products_list.append(products_value)


        return products_list

