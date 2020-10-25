from report.texts import Text
from typing import List

class Question_1:
    def __init__(self, answer: str):
        self.answer = answer
        self.ANSWER_VERY_SHORT = "Very short"
        self.ANSWER_SHORT = "Short"
        self.ANSWER_MEDIUM = "Medium"
        self.ANSWER_LONG = "Long"

    def get_answer(self):
        if (
            self.answer == self.ANSWER_VERY_SHORT
        ):
            return Text.ANSWER_VERY_SHORT

        if (
            self.answer == self.ANSWER_SHORT
        ):
            return Text.ANSWER_SHORT

        if (
            self.answer == self.ANSWER_MEDIUM
        ):
            return Text.ANSWER_MEDIUM

        if (
            self.answer == self.ANSWER_LONG
        ):
            return Text.ANSWER_LONG

class Question_2:
    def __init__(self, answer: str):
        self.answer = answer
        self.ANSWER_EVERYDAY = "Everyday"
        self.ANSWER_2_TIMES = "2 times a week"
        self.ANSWER_1_TIME = "1 time a week"
        self.ANSWER_3_TIMES = "3 times a week"

    def get_answer(self):
        if (
            self.answer == self.ANSWER_EVERYDAY or
            self.answer == self.ANSWER_2_TIMES
        ):
            return Text.ANSWER_EVERDAY_AND_ANSWER_2_TIMES

        if (
            self.answer == self.ANSWER_1_TIME or
            self.answer == self.ANSWER_3_TIMES
        ):
            return Text.ANSWER_1_TIME_AND_ANSWER_3_TIMES

class Question_3:
    def __init__(self, answer: str):
        self.answer = answer
        self.ANSWER_DANDRUFF = "Dandruff"
        self.ANSWER_HAIR_LOSS = "Hair loss"
        self.ANSWER_DRY_HAIR = "Dry hair"
        self.ANSWER_PSORIASIS = "Psoriasis"
        self.ANSWER_HEAD_LICE = "Head lice"
        self.ANSWER_BAMBOO_HAIR = "Bamboo hair"
        self.ANSWER_VERY_OILY_HAIR = "Very oily hair"

    def get_answer(self):
        if (
            self.ANSWER_PSORIASIS in self.answer and
            self.ANSWER_DRY_HAIR in self.answer and
            self.ANSWER_DANDRUFF in self.answer
        ):
            return Text.QUESTION_3_ANSWER_1

        elif (
            self.ANSWER_HAIR_LOSS in self.answer and
            self.ANSWER_HEAD_LICE in self.answer
        ):
            return Text.QUESTION_3_ANSWER_2

        elif (
            self.ANSWER_VERY_OILY_HAIR in self.answer and
            self.ANSWER_DRY_HAIR in self.answer or
            self.ANSWER_DANDRUFF in self.answer
        ):
            return Text.QUESTION_3_ANSWER_3

        else:
            return Text.QUESTION_3_ANSWER_3_else

class Question_4:
    def __init__(self, answer_cur: str, answer_pr: int):
        self.answer_currency = answer_cur
        self.answer_price = answer_pr
        self.ANSWER_EUR = "Eur"
        self.ANSWER_USD = "USD"
        self.ANSWER_120 = 120
        self.ANSWER_265 = 265
        self.ANSWER_60 = 60
        self.ANSWER_132 = 132

    def get_answer(self):
        if (
            self.answer_price > self.ANSWER_120 and
            self.answer_currency == self.ANSWER_EUR or
            self.answer_price > self.ANSWER_265 and
            self.answer_currency == self.ANSWER_USD
        ):
            return Text().get_PRICE_first_MULTIPLY(
                calculation=round(self.answer_price * 1.3)
            )

        elif (
            self.answer_price < self.ANSWER_60 and
            self.answer_currency == self.ANSWER_EUR or
            self.answer_price < self.ANSWER_132 and
            self.answer_currency == self.ANSWER_USD
        ):
            return Text().get_PRICE_second_MULTIPLY(
                calculation=round(self.answer_price * 1.3 * 1.1)
            )

        else:
            return Text().get_PRICE_third_MULTIPLY(
                calculation=round(self.answer_price * 1.3 * 15.2)
            )

class Question_5:
    def __init__(self, answer_choice: str, answer_yes_choices: List):
        self.answer_choice = answer_choice
        self.answer_yes_choices = answer_yes_choices
        self.ANSWER_YES = "Yes"
        self.ANSWER_IDK = "I don't know"
        self.NO = "No"

    def get_answer(self):
        if (
            self.answer_choice == self.ANSWER_IDK
        ):
            return Text.ANSWER_IDK

        if (
            self.answer_choice  == self.NO
        ):
            return Text.ANSWER_NO

        if (
            self.answer_choice == self.ANSWER_YES and
            ["Applying lemon"] and
            ["Applying garlic water"] in
            self.answer_yes_choices
        ):
            return Text.ANSWER_YES_lemon_garlicwater

        if (
            self.answer_choice == self.ANSWER_YES and
            ["Applying Aloe liquid"] and
            ["Do not washing"] in
            self.answer_yes_choices
        ):
            return Text.ANSWER_YES_aloe_not_washing

        else:
            return Text.ANSWER_YES_else