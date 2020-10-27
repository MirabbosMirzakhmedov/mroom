from typing import Dict

class Survey:

    def __init__(self, answers):
        self.answers = answers

questions_answers: Dict = {
    'Q1_answer': "Very short",
    'Q2_answer': "Everyday",
    'Q3_answer': ["Dandruff", "Hair loss", "Dry hair",
                  "Psoriasis", "Head lice", "Bamboo hair", "Very oily hair"],
    'Q4_answer': {
        "price": 120,
        "currency": "Eur",
    },
    'Q5_answer': {
        "choice": "Yes",
        "yes_choices": ["Applying Aloe liquid", "Applying lemon",
                        "Applying garlic water", "Do not washing"]
    },
}