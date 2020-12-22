from typing import List, Dict

a: Dict = {
    'asin': 'B08BGD4G36',
    'title': 'dsadsadsa',
    'image': 'dsadsadsa',
    'full_link': 'dsadsadas',
    'prices': {
        'current_price': 500,
        'previous_price': 476.09,
        'currency': '$'
    },
    'reviews': {
        'total_reviews': 16402,
        'stars': 4.5
    },
    'prime': False
}



print(a['prices']['currency'])
