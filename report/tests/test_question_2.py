import unittest

from report.questions import Question
from report.tests.test_data.question_texts import TestTest


class TestQuestionTwo(unittest.TestCase):

    def test_answer_1(self):
        actual_result: str = Question(
            "Everyday"
        ).get_how_often_do_you_wash_your_hair_answer()

        expected_result: str = TestTest.ANSWER_EVERDAY_AND_ANSWER_2_TIMES

        self.assertEqual(actual_result, expected_result)

    def test_answer_2(self):
        actual_result: str = Question(
            "2 times a week"
        ).get_how_often_do_you_wash_your_hair_answer()

        expected_result: str = TestTest.ANSWER_EVERDAY_AND_ANSWER_2_TIMES

        self.assertEqual(actual_result, expected_result)

    def test_answer_3(self):
        actual_result: str = Question(
            "1 time a week"
        ).get_how_often_do_you_wash_your_hair_answer()

        expected_result: str = TestTest.ANSWER_1_TIME_AND_ANSWER_3_TIMES

        self.assertEqual(actual_result, expected_result)

    def test_answer_4(self):
        actual_result: str = Question(
            "3 times a week"
        ).get_how_often_do_you_wash_your_hair_answer()

        expected_result: str = TestTest.ANSWER_1_TIME_AND_ANSWER_3_TIMES

        self.assertEqual(actual_result, expected_result)
        