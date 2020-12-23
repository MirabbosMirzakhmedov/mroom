from typing import List, Dict

a: List = [
    {
        'results': [
            {
                'asin': 'B08BGD4G36',
                'title': 'Apple iPhone XR, 64GB, White - Fully Unlocked (Renewed Premium)',
                'image': 'https://m.media-amazon.com/images/I/41ZjUOH6nRL._AC_UY218_.jpg',
                'full_link': 'https://www.amazon.com/dp/B08BGD4G36/?psc=1',
                'prices': {
                    'current_price': 135.0,
                    'previous_price': 476.09,
                    'currency': '$'
                },
                'reviews': {
                    'total_reviews': 16402,
                    'stars': 4.5
                },
                'prime': False
            },

        ]
    }
]

product: Dict = {
    'asin': 'B08BGD4G36',
    'title': 'Apple iPhone XR, 64GB, White - Fully Unlocked (Renewed Premium)',
    'image': 'https://m.media-amazon.com/images/I/41ZjUOH6nRL._AC_UY218_.jpg',
    'full_link': 'https://www.amazon.com/dp/B08BGD4G36/?psc=1',
    'prices': {
        'current_price': 135.0,
        'previous_price': 476.09,
        'currency': '$'
    },
    'reviews': {
        'total_reviews': 16402,
        'stars': 4.5
    },
    'prime': False
}

print(product['prices']['currency'])


products: List = [
    {
        'title': 'Apple iPhone XR, 64GB, White - Fully Unlocked (Renewed Premium)',
        'image': 'https://m.media-amazon.com/images/I/41ZjUOH6nRL._AC_UY218_.jpg',
        'full_link': 'https://www.amazon.com/dp/B08BGD4G36/?psc=1',
        'current_price': 135.0,
        'currency': '$'
    }
]

print(products[0]['currency'])

