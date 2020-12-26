import unittest
import requests, random

from typing import Dict, List
from unittest.mock import patch, Mock

from products.parse import Products
from products.request import ProductRequest


class MockResponse:
    def __init__(self):
        pass

    def get_product(
            self,
            current_price: float,
            title: str = 'Apple iPhone XR, 64GB, '
                         'White - Fully Unlocked (Renewed Premium)',
            image: str = 'https://m.media-amazon.com/'
                         'images/I/41ZjUOH6nRL._AC_UY218_.jpg',
            full_link: str = 'https://www.amazon.com/dp/B08BGD4G36/?psc=1',
            currency: str = '$',
    ) -> Dict:
        return {
            'asin': 'B08BGD4G36',
            'title': title,
            'image': image,
            'full_link': full_link,
            'prices': {
                'current_price': current_price,
                'previous_price': 476.09,
                'currency': currency
            },
            'reviews': {
                'total_reviews': 16402,
                'stars': 4.5
            },
            'prime': False
        }

    def get_products(self, invalid_products: List) -> Mock:
        mock_response: Mock = Mock()
        mock_response.status_code = 200

        valid_products: List = [
            self.get_product(current_price=7.0) for _ in range(10)
        ]

        products = invalid_products + valid_products
        random.shuffle(products)

        mock_response.json.return_value = {
            'results': products
        }
        return mock_response

    def get_products_price_higher_than_minus_one(
            self,
            *args,
            **kwargs
    ) -> Mock:
        return self.get_products(
            invalid_products=[
                self.get_product(
                    current_price=-1.0
                ) for _ in range(10)
            ]
        )

    def get_products_valid_and_invalid_title(
            self,
            *args,
            **kwargs
    ) -> Mock:
        return self.get_products(
            invalid_products=[
                self.get_product(
                    current_price=7.0,
                    title=''
                ) for _ in range(10)
            ]
        )

    def get_products_valid_and_invalid_image(
            self,
            *args,
            **kwargs
    ) -> Mock:
        invalid_image_url: List = [
            self.get_product(
                current_price=7.0,
                image='asdadsa'
            ) for _ in range(5)
        ]

        empty_image_url: List = [
            self.get_product(
                current_price=7.0,
                image=''
            ) for _ in range(5)
        ]

        products = invalid_image_url + empty_image_url
        random.shuffle(products)

        return self.get_products(
            invalid_products=products
        )

    def get_products_valid_and_invalid_full_link(
            self,
            *args,
            **kwargs
    ) -> Mock:
        empty_full_link: List = [
            self.get_product(
                current_price=7.0,
                full_link=''
            ) for _ in range(5)
        ]

        valid_full_link: List = [
            self.get_product(
                current_price=7.0,
                full_link='https://www.amazon.com/dp/B08BGD4G36/?psc=1'
            ) for _ in range(5)
        ]

        products = empty_full_link + valid_full_link
        random.shuffle(products)

        return self.get_products(
            invalid_products=products
        )

    def get_products_valid_and_invalid_currency(
            self,
            *args,
            **kwargs
    ) -> Mock:
        invalid_currency: List = [
            self.get_product(
                current_price=7.0,
                currency=''
            ) for _ in range(5)
        ]

        valid_currency: List = [
            self.get_product(
                current_price=7.0,
                currency='$'
            ) for _ in range(5)
        ]

        products = invalid_currency + valid_currency
        random.shuffle(products)

        return self.get_products(
            invalid_products=products
        )

    def get_products_price_higher_than_five_usd(
            self,
            *args,
            **kwargs
    ) -> Mock:
        return self.get_products(
            invalid_products=[
                self.get_product(
                    current_price=3.0
                ) for _ in range(10)
            ]
        )


class TestProducts(unittest.TestCase):
    def execute_request_and_get_products(self) -> List:

        request = ProductRequest()

        res: requests.Response = request.get(
            params={
                'country': 'US',
                'query': 'Shampoo',
            }
        )

        for product in res.json()['results']:
            print("product['prices']: ", product['prices']['current_price'])

        return Products(
            res_data=res.json(),
            amount=5,
        ).get()

    @patch.object(
        requests,
        'get',
        side_effect=MockResponse().get_products_price_higher_than_minus_one
    )
    def test_products_price_higher_than_minus_one(self, *args, **kwargs):
        products: List = self.execute_request_and_get_products()

        for product in products:
            self.assertEqual(product['current_price'] > -1.0, True)

    @patch.object(
        requests,
        'get',
        side_effect=MockResponse().get_products_valid_and_invalid_title
    )
    def test_products_has_valid_name(self, *args, **kwargs):
        products: List = self.execute_request_and_get_products()

        for product in products:
            self.assertNotEqual(product['title'], '')

    @patch.object(
        requests,
        'get',
        side_effect=MockResponse().get_products_valid_and_invalid_image
    )
    def test_products_has_invalid_image(self, *args, **kwargs):
        products: List = self.execute_request_and_get_products()

        for product in products:
            extension = product['image'].split('.')[-1]

            actual_result = extension == 'jpg'
            expected_result = True

            self.assertEqual(actual_result, expected_result)

    @patch.object(
        requests,
        'get',
        side_effect=MockResponse().get_products_valid_and_invalid_full_link
    )
    def test_products_has_invalid_full_link(self, *args, **kwargs):
        products: List = self.execute_request_and_get_products()

        for product in products:
            self.assertNotEqual(product['full_link'], '')

    @patch.object(
        requests,
        'get',
        side_effect=MockResponse().get_products_valid_and_invalid_currency
    )
    def test_products_has_invalid_currency(self, *args, **kwargs):
        products: List = self.execute_request_and_get_products()

        for product in products:
            actual_result = product['currency'] != '$'
            expected_result = False

            self.assertEqual(actual_result, expected_result)

    @patch.object(
        requests,
        'get',
        side_effect=MockResponse().get_products_price_higher_than_five_usd
    )
    def test_products_price_higher_than_five_usd(self, *args, **kwargs):
        products: List = self.execute_request_and_get_products()

        for product in products:
            actual_result = product['current_price'] <= 5.0
            expected_result = False

            self.assertEqual(actual_result, expected_result)
