import unittest

from report.questions import Question
from report.tests.test_data.question_texts import TestTest


class TestQuestionOne(unittest.TestCase):

    def test_answer_1(self):
        actual_result: str = Question(
            "Very short"
        ).get_how_long_hair_do_you_have_answer()

        expected_result: str = TestTest.ANSWER_VERY_SHORT

        self.assertEqual(actual_result, expected_result)

    def test_answer_2(self):
        actual_result: str = Question(
            "Short"
        ).get_how_long_hair_do_you_have_answer()

        expected_result: str = TestTest.ANSWER_SHORT

        self.assertEqual(actual_result, expected_result)

    def test_answer_3(self):
        actual_result: str = Question(
            "Medium"
        ).get_how_long_hair_do_you_have_answer()

        expected_result: str = TestTest.ANSWER_MEDIUM

        self.assertEqual(actual_result, expected_result)

    def test_answer_4(self):
        actual_result: str = Question(
            "Long"
        ).get_how_long_hair_do_you_have_answer()

        expected_result: str = TestTest.ANSWER_LONG

        self.assertEqual(actual_result, expected_result)
