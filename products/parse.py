from typing import Dict, List


class Products:

    def __init__(self, res_data: Dict, amount: int):
        self.data = res_data
        self.amount = amount

    def get(self) -> List:

        products: List = []


        for product in self.data['results']:

            if product['prices']['current_price'] == -1.0:
                continue

            if product['title'] == '':
                continue

            if product['image'].split('.')[-1] != 'jpg':
                continue
            #
            if product['full_link'] != 'www.amazon.com':
                continue
            #
            if product['prices']['currency'] != '$':
                continue

            # if product['prices']['current_price'] == 5:
            #     continue

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

