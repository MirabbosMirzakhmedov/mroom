from typing import Dict, List
import requests

class ProductRequest:

    def __init__(self):
        self.url: str = 'https://amazon-products1.p.rapidapi.com/search'
        self.headers: Dict = {
            'x-rapidapi-key':
                'a8f0a072d2msh3d1bfc104318241p1aec10jsn70718bbf81a2',
            'x-rapidapi-host':
                'amazon-products1.p.rapidapi.com'
        }
        self.timeout: int = 20

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
product: Dict = res_data['results'][0]

def get_products(res_data: Dict) -> List:
    products: List = []

    for product in res_data['results']:

        if product['prices']['current_price'] > -1.0:
            products.append(
                {
                    'title': product['title'],
                    'image': product['image'],
                    'full_link': product['full_link'],
                    'current_price': product['prices']['current_price'],
                    'currency': product['prices']['currency'],
                }
            )

        if len(products) == 5:
            break

    return products

five_products: List = get_products(res_data)

class Products:

    def __init__(self, res_data: Dict, amount: int):
        self.data = res_data
        self.amount = amount

    def get(self) -> List:

        products: List = []

        for product in self.data['results']:

            if product['prices']['current_price'] > -1.0:
                products.append(
                    {
                        'title': product['title'],
                        'image': product['image'],
                        'full_link': product['full_link'],
                        'current_price': product['prices']['current_price'],
                        'currency': product['prices']['currency'],
                    }
                )

            if len(products) == self.amount:
                break

        return products

products = Products(
    res_data=res_data,
    amount=5
).get()

with open(
        'D:\Python Mentorship\module_5\project_exercise\products_list.txt',
        'w') as f:

    for list_num, product in enumerate(products):

        f.write(
            f'Product #{list_num}:\n'
            f'\t{product["title"]}\n'
            f'\tPrice: {product["prices"]["currency"]}{product["current_price"]}\n'
            f'\tLink: {product["full_link"]}\n\n')
    f.close()