import unittest

from report.questions import Question
from report.tests.test_data.question_texts import TestTest

class TestQuestionFive(unittest.TestCase):

    def test_answer_1(self):
        actual_result: str = Question(
            {"choice": "I don't know"}
            ).get_solutions_you_can_do_at_home_answer()

        expected_result: str = TestTest.ANSWER_IDK

        self.assertEqual(actual_result, expected_result)

    def test_answer_2(self):
        actual_result: str = Question(
            {"choice": "No"}
            ).get_solutions_you_can_do_at_home_answer()

        expected_result: str = TestTest.ANSWER_NO

        self.assertEqual(actual_result, expected_result)

    def test_answer_3(self):
        actual_result: str = Question(
            {
                "choice": "Yes",
                "yes_choices": ["Applying lemon",
                                "Applying garlic water"]
            }
            ).get_solutions_you_can_do_at_home_answer()

        expected_result: str = TestTest.ANSWER_YES_lemon_garlicwater

        self.assertEqual(actual_result, expected_result)

    def test_answer_4(self):
        actual_result: str = Question(
            {
                "choice": "Yes",
                "yes_choices": ["Applying Aloe liquid",
                                "Do not washing"]
            }
            ).get_solutions_you_can_do_at_home_answer()

        expected_result: str = TestTest.ANSWER_YES_aloe_not_washing

        self.assertEqual(actual_result, expected_result)

    def test_answer_5(self):
        actual_result: str = Question(
            {
                "choice": "Wrong inserted message"
            }
            ).get_solutions_you_can_do_at_home_answer()

        expected_result: str = TestTest.ANSWER_YES_else

        self.assertEqual(actual_result, expected_result)



