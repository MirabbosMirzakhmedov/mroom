from typing import Dict
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

    def get(self, params: Dict) -> requests.Response:
        return requests.get(
            url=self.url,
            header=self.headers,
            timeout=self.timeout,
            params=params
        )
