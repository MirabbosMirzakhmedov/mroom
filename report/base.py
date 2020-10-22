from typing import Dict
from report.questions import \
    Question_1, Question_2, Question_3, \
    Question_4, Question_5



class Report:
    def __init__(self, questions: List):
        self.questions = questions

    def get(self):
        text: str = ""
        for question in self.questions:
            text += question.get_answer()
        return text

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

report = Report(
    questions=[
        Question_1(questions_answers["Q1_answer"]),
        Question_2(questions_answers["Q2_answer"]),
        Question_3(questions_answers["Q3_answer"]),
        Question_4(answer_cur="Eur", answer_pr=120),
        Question_5(
            answer_choice="Yes",
            answer_yes_choices=["Applying Aloe liquid",
                                "Applying lemon",
                                "Applying garlic water",
                                "Do not washing"]
        )
    ]
)

report_text: str = report.get()

print(report_text)
