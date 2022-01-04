import unittest

from report.questions import Question
from report.tests.test_data.question_texts import TestTexts


class TestQuestionFive(unittest.TestCase):

    def test_answer_i_dont_know(self):
        actual_result: str = Question(
            {'choice': "I don't know"}
        ).get_solutions_you_can_do_at_home_answer()

        expected_result: str = TestTexts.ANSWER_IDK

        self.assertEqual(actual_result, expected_result)

    def test_answer_no(self):
        actual_result: str = Question(
            {'choice': 'No'}
        ).get_solutions_you_can_do_at_home_answer()

        expected_result: str = TestTexts.ANSWER_NO

        self.assertEqual(actual_result, expected_result)

    def test_answer_yes_lemon_garlic_water(self):
        actual_result: str = Question(
            {
                'choice': 'Yes',
                'yes_choices': ['Applying lemon',
                                'Applying garlic water']
            }
        ).get_solutions_you_can_do_at_home_answer()

        expected_result: str = TestTexts.ANSWER_YES_lemon_garlicwater

        self.assertEqual(actual_result, expected_result)

    def test_answer_yes_aloe_liquid_dont_wash(self):
        actual_result: str = Question(
            {
                'choice': 'Yes',
                'yes_choices': ['Applying Aloe liquid',
                                'Do not washing']
            }
        ).get_solutions_you_can_do_at_home_answer()

        expected_result: str = TestTexts.ANSWER_YES_aloe_not_washing

        self.assertEqual(actual_result, expected_result)

    def test_answer_wrong_message(self):
        actual_result: str = Question(
            {
                'choice': 'Wrong inserted message'
            }
        ).get_solutions_you_can_do_at_home_answer()

        expected_result: str = TestTexts.ANSWER_YES_else

        self.assertEqual(actual_result, expected_result)
