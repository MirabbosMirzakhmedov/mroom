import unittest

from mroom.report.questions import Question
from mroom.report.tests.test_data.question_texts import TestTest


class Test_Question_2(unittest.TestCase):
    def test_question_1_Everyday(self):
        actual_result: str = Question(
            "Everyday"
        ).get_how_often_do_you_wash_your_hair_answer()

        expected_result: str = TestTest.ANSWER_EVERDAY_AND_ANSWER_2_TIMES

        self.assertEqual(actual_result, expected_result)

    def test_question_2_TWO_TIMES(self):
        actual_result: str = Question(
            "2 times a week"
        ).get_how_often_do_you_wash_your_hair_answer()

        expected_result: str = TestTest.ANSWER_EVERDAY_AND_ANSWER_2_TIMES

        self.assertEqual(actual_result, expected_result)

    def test_question_3_ONE_TIME(self):
        actual_result: str = Question(
            "1 time a week"
        ).get_how_often_do_you_wash_your_hair_answer()

        expected_result: str = TestTest.ANSWER_1_TIME_AND_ANSWER_3_TIMES

        self.assertEqual(actual_result, expected_result)

    def test_question_4_THREE_TIMES(self):
        actual_result: str = Question(
            "3 times a week"
        ).get_how_often_do_you_wash_your_hair_answer()

        expected_result: str = TestTest.ANSWER_1_TIME_AND_ANSWER_3_TIMES

        self.assertEqual(actual_result, expected_result)
        