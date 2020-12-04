from typing import Union, Dict

data: Dict = {
    'error': False,
    'results': [
        {
            'asin': 'B08J115RZL',
            'title': 'Head & Shoulders Clinical Strength Dandruff Shampoo Twin Pack, Itensive Itch Relief with Cooling Menthol, 13.5 Oz Each',
            'image': 'https://m.media-amazon.com/images/I/81505x3GzOL._AC_UL320_.jpg',
            'full_link': 'https://www.amazon.com/dp/B08J115RZL/?psc=1',
            'prices':
                {
                    'current_price': 18.0,
                    'previous_price': -1.0,
                    'currency': '$'
                },
            'reviews': {
                'total_reviews': 1318,
                'stars': 4.6
            },
            'prime': False
        }
    ]
}

price: Union = data['results'][0]['prices']['current_price']
currency: Union = data['results'][0]['prices']['currency']

print(price)
print(currency)