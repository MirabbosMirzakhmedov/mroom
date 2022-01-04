from typing import List

from report.questions import Question
from survey.base import Survey


class Report:
    def __init__(self, survey: Survey):
        self.survey = survey

    def get_question_answers(self) -> List:
        return [
            Question(
                self.survey.answers['Q1_answer']
            ).get_how_long_hair_do_you_have_answer(),
            Question(
                self.survey.answers['Q2_answer']
            ).get_how_often_do_you_wash_your_hair_answer(),
            Question(
                self.survey.answers['Q3_answer']
            ).get_what_kind_of_problems_do_you_have_answer(),
            Question(
                self.survey.answers['Q4_answer']
            ).get_whats_the_price_for_your_shampoo_answer(),
            Question(
                self.survey.answers['Q5_answer']
            ).get_solutions_you_can_do_at_home_answer(),

        ]

    def get(self) -> str:
        text: str = ''
        for answer_text in self.get_question_answers():
            text += answer_text
        return text


survey = Survey(
    answers={
        'Q1_answer': 'Very short',
        'Q2_answer': 'Everyday',
        'Q3_answer': ['Dandruff', 'Hair loss', 'Dry hair',
                      'Psoriasis', 'Head lice', 'Bamboo hair',
                      'Very oily hair'],
        'Q4_answer': {
            'price': 120,
            'currency': 'Eur',
        },
        'Q5_answer': {
            'choice': 'Yes',
            'yes_choices': ['Applying Aloe liquid', 'Applying lemon',
                            'Applying garlic water', 'Do not washing']
        },
    }
)

report = Report(survey=survey)
report_text: str = report.get()

print(report_text)
