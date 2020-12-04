#TODO: Exercise 6: Create 'get_products' function
# 1. Create a new function called 'get_products'
# 2. 'get_products' function takes 1 argument 'res_data'
# 3. The goal of the function is to return a list of 5 products
# 4.
# 4. Each product should be appended to the 'products' list
#    as a Dict with with product 'title', 'image', 'full_link', 'current_price', 'currency'
# 5. Use 'for loop' to with 'break' statement to end the 'for loop' once you have collected 5 products
# 6. Use if statement to only add products with current_price higher than -1.0 (float)
# 7. The function should return a list of products (add a return type to the function)

from products.exercise_5 import products
from typing import Dict, List



def get_products(res_data) -> List:

    products_value: Dict = {}
    products_list: List = []

    # for products[0] in res_data :
    #     products_value += res_data
    #     products_list.append(products_value)

    for products[0] in res_data:
        res_data += products_value
        products_list.append(products_value)

        return products_list










    