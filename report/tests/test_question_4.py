import unittest

from report.questions import Question
from report.tests.test_data.question_texts import TestTexts

class TestQuestionFour(unittest.TestCase):

    def test_answer_bigger_than_120_eur(self):
        test_price: int = 121
        # Here, the test price must be bigger than 120.

        actual_result = Question(
                {
                    'price': test_price,
                    'currency': 'Eur',
                }
            ).get_whats_the_price_for_your_shampoo_answer()

        expected_result: str =\
            TestTexts.QUESTION_4_HIGHER_THAN_120_EUR

        # self.assertEqual(actual_result, expected_result)
        self.assertEqual(expected_result, actual_result)

    def test_answer_bigger_than_265_USD(self):
        test_price: int = 266
        # Here, the test price must be bigger than 265

        actual_result = Question(
                {
                    'price': test_price,
                    'currency': 'USD',
                }
            ).get_whats_the_price_for_your_shampoo_answer()

        expected_result: str =\
            TestTexts.QUESTION_4_HIGHER_THAN_265_USD

        self.assertEqual(actual_result, expected_result)

    def test_answer_smaller_than_60_eur(self):
        test_price: int = 59
        # Here the test price must be smaller than 60

        actual_result = Question(
                {
                    'price': test_price,
                    'currency': 'Eur',
                }
            ).get_whats_the_price_for_your_shampoo_answer()

        expected_result: str =\
            TestTexts.QUESTION_4_LOWER_THAN_60_EUR

        self.assertEqual(actual_result, expected_result)

    def test_answer_smaller_than_132_USD(self):
        test_price: int = 131
        # Here, the test price must be smaller than 132

        actual_result = Question(
                {
                    'price': test_price,
                    'currency': 'USD',
                }
            ).get_whats_the_price_for_your_shampoo_answer()

        expected_result: str =\
            TestTexts.QUESTION_4_LOWER_THAN_132_USD

        self.assertEqual(actual_result, expected_result)

    def test_answer_any_other_case(self):
        test_price: int = 100
        test_currency: str = 'PRC'
        # Optional condition to check the last option

        actual_result = Question(
                {
                    'price': test_price,
                    'currency': test_currency,
                }
            ).get_whats_the_price_for_your_shampoo_answer()

        expected_result: str = TestTexts.QUESTION_4_ANY_OTHER_CASE

        self.assertEqual(actual_result, expected_result)
