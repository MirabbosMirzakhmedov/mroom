from typing import List
from survey.base import Survey
from report.questions import (
    Question_1,
    Question_2,
    Question_3,
    Question_4,
    Question_5,
)

class Report:
    def __init__(self, survey: Survey):
        self.survey = survey

    def get_questions(self):
        return [
            Question_1(self.survey.answers["Q1_answer"]),
            Question_2(self.survey.answers["Q2_answer"]),
            Question_3(self.survey.answers["Q3_answer"]),
            Question_4(answer_currency="Eur", answer_price=120),
            Question_5(
                answer_choice="Yes",
                answer_yes_choices=["Applying Aloe liquid",
                                    "Applying lemon",
                                    "Applying garlic water",
                                    "Do not washing"]
            )
        ]

    def get(self):
        text: str = ""
        for question in self.get_questions():
            text += question.get_answer()
        return text

survey = Survey(
    answers={
        'Q1_answer': "Very short",
        'Q2_answer': "Everyday",
        'Q3_answer': ["Dandruff", "Hair loss", "Dry hair",
                      "Psoriasis", "Head lice", "Bamboo hair",
                      "Very oily hair"],
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
)

report = Report(survey=survey)
report_text: str = report.get()