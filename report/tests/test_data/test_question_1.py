import unittest

from mroom.report.questions import Question
from mroom.report.tests.test_data.question_texts import TestTest


class Test_Question_1(unittest.TestCase):

    def test_question_1_very_short(self):
        actual_result: str = Question(
            'Very short'
        ).get_how_long_hair_do_you_have_answer()
        expected_result: str = TestTest.ANSWER_VERY_SHORT

        self.assertEqual(actual_result, expected_result)

    def test_question_2_short(self):
        actual_result: str = Question(
            "Short"
        ).get_how_long_hair_do_you_have_answer()

        expected_result: str = TestTest.ANSWER_SHORT

        self.assertEqual(actual_result, expected_result)

    def test_question_3_medium(self):
        actual_result: str = Question(
            "Medium"
        ).get_how_long_hair_do_you_have_answer()

        expected_result: str = TestTest.ANSWER_MEDIUM

        self.assertEqual(actual_result, expected_result)

    def test_question_4_Long(self):
        actual_result: str = Question(
            "Long"
        ).get_how_long_hair_do_you_have_answer()

        expected_result: str = TestTest.ANSWER_LONG

        self.assertEqual(actual_result, expected_result)
