import unittest

from report.questions import Question
from report.tests.test_data.question_texts import TestTest

class TestQuestionFour(unittest.TestCase):

    def test_answer_1(self):
        test_price: int = 121
        # Here, the test price must be bigger than 120.

        actual_result = Question(
                {
                    "price": test_price,
                    "currency": "Eur",
                }
            ).get_whats_the_price_for_your_shampoo_answer()

        expected_result: str = TestTest().get_price_higher_than_120_or_265(
            calculation=round(test_price * 1.3)
        )

        self.assertEqual(actual_result, expected_result)

    def test_answer_2(self):
        test_price: int = 266
        # Here, the test price must be bigger than 265

        actual_result = Question(
                {
                    "price": test_price,
                    "currency": "USD",
                }
            ).get_whats_the_price_for_your_shampoo_answer()

        expected_result: str = TestTest().get_price_higher_than_120_or_265(
            calculation=round(test_price * 1.3)
        )

        self.assertEqual(actual_result, expected_result)

    def test_answer_3(self):
        test_price: int = 59
        # Here the test price must be smaller than 60

        actual_result = Question(
                {
                    "price": test_price,
                    "currency": "Eur",
                }
            ).get_whats_the_price_for_your_shampoo_answer()

        expected_result: str = TestTest().get_price_lower_than_60_or_132(
            calculation=round(test_price * 1.3 * 1.1)
        )

        self.assertEqual(actual_result, expected_result)

    def test_answer_4(self):
        test_price: int = 131
        # Here, the test price must be smaller than 132

        actual_result = Question(
                {
                    "price": test_price,
                    "currency": "USD",
                }
            ).get_whats_the_price_for_your_shampoo_answer()

        expected_result: str = TestTest().get_price_lower_than_60_or_132(
            calculation=round(test_price * 1.3 * 1.1)
        )

        self.assertEqual(actual_result, expected_result)

    def test_answer_any_other_case(self):
        test_price: int = 100
        test_currency: str = "PRC"
        # Optional condition to check the last option

        actual_result = Question(
                {
                    "price": test_price,
                    "currency": test_currency,
                }
            ).get_whats_the_price_for_your_shampoo_answer()

        expected_result: str = TestTest().get_price_any_other_case(
            calculation=round(test_price * 1.3 * 15.2)
        )

        self.assertEqual(actual_result, expected_result)






