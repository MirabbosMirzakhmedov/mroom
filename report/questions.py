from typing import (
    List,
    Dict,
    Union,
)

from report.texts import Text


class Answers:
    VERY_SHORT = 'Very short'
    SHORT = 'Short'
    MEDIUM = 'Medium'
    LONG = 'Long'

    EVERYDAY = 'Everyday'
    TWO_TIMES = '2 times a week'
    ONE_TIME = '1 time a week'
    THREE_TIMES = '3 times a week'

    DANDRUFF = 'Dandruff'
    HAIR_LOSS = 'Hair loss'
    DRY_HAIR = 'Dry hair'
    PSORIASIS = 'Psoriasis'
    HEAD_LICE = 'Head lice'
    BAMBOO_HAIR = 'Bamboo hair'
    VERY_OILY_HAIR = 'Very oily hair'

    EUR = 'Eur'
    USD = 'USD'
    price_120 = 120
    price_265 = 265
    price_60 = 60
    price_132 = 132

    YES = 'Yes'
    IDK = "I don't know"
    NO = 'No'


class Question:

    def __init__(
            self,
            answer: Union[str, Dict, List],
    ):
        self.answer = answer
        self.text = Text()

        if isinstance(self.answer, Dict):
            self.currency = self.answer.get('currency')
            self.price = self.answer.get('price')
            self.answer_choice = self.answer.get('choice')
            self.answer_yes_choices = self.answer.get('yes_choices')

    # FIRST QUESTION
    def get_how_long_hair_do_you_have_answer(self):
        if (
                self.answer == Answers.VERY_SHORT
        ):
            return self.text.ANSWER_VERY_SHORT

        if (
                self.answer == Answers.SHORT
        ):
            return self.text.ANSWER_SHORT

        if (
                self.answer == Answers.MEDIUM
        ):
            return self.text.ANSWER_MEDIUM

        if (
                self.answer == Answers.LONG
        ):
            return self.text.ANSWER_LONG

    # SECOND QUESTION
    def get_how_often_do_you_wash_your_hair_answer(self):
        if (
                self.answer == Answers.EVERYDAY or
                self.answer == Answers.TWO_TIMES
        ):
            return self.text.ANSWER_EVERDAY_AND_ANSWER_2_TIMES

        if (
                self.answer == Answers.ONE_TIME or
                self.answer == Answers.THREE_TIMES
        ):
            return self.text.ANSWER_1_TIME_AND_ANSWER_3_TIMES

    # THIRD QUESTION
    def get_what_kind_of_problems_do_you_have_answer(self):
        if (
                Answers.PSORIASIS in self.answer and
                Answers.DRY_HAIR in self.answer and
                Answers.DANDRUFF in self.answer
        ):
            return self.text.QUESTION_3_ANSWER_1

        elif (
                Answers.PSORIASIS in self.answer and
                Answers.HEAD_LICE in self.answer
        ):
            return self.text.QUESTION_3_ANSWER_2

        elif (
                Answers.VERY_OILY_HAIR in self.answer and
                Answers.DRY_HAIR in self.answer or
                Answers.DANDRUFF in self.answer
        ):
            return self.text.QUESTION_3_ANSWER_3

        else:
            return self.text.QUESTION_3_ANSWER_3_else

    # FOURTH QUESTION
    def get_whats_the_price_for_your_shampoo_answer(self):
        if (
                self.price > Answers.price_120 and
                self.currency == Answers.EUR or
                self.price > Answers.price_265 and
                self.currency == Answers.USD
        ):
            return Text().get_price_higher_than_120_or_265(
                calculation=round(self.price * 1.3)
            )

        elif (
                self.price < Answers.price_60 and
                self.currency == Answers.EUR or
                self.price < Answers.price_132 and
                self.currency == Answers.USD
        ):
            return Text().get_price_lower_than_60_or_132(
                calculation=round(self.price * 1.3 * 1.1)
            )

        else:
            return Text().get_price_any_other_case(
                calculation=round(self.price * 1.3 * 15.2)
            )

    # FIFTH QUESTION
    def get_solutions_you_can_do_at_home_answer(self):
        if (
                self.answer_choice == Answers.IDK
        ):
            return self.text.ANSWER_IDK

        if (
                self.answer_choice == Answers.NO
        ):
            return self.text.ANSWER_NO

        if (
                self.answer_choice == Answers.YES and
                'Applying lemon' in self.answer_yes_choices and
                'Applying garlic water' in self.answer_yes_choices
        ):
            return self.text.ANSWER_YES_lemon_garlicwater

        if (
                self.answer_choice == Answers.YES and
                'Applying Aloe liquid' in self.answer_yes_choices and
                'Do not washing' in self.answer_yes_choices
        ):
            return self.text.ANSWER_YES_aloe_not_washing

        else:
            return self.text.ANSWER_YES_else
