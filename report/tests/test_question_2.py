import unittest

from report.questions import Question
from report.tests.test_data.question_texts import TestTexts


class TestQuestionTwo(unittest.TestCase):

    def test_answer_everyday(self):
        actual_result: str = Question(
            "Everyday"
        ).get_how_often_do_you_wash_your_hair_answer()

        expected_result: str = TestTexts.ANSWER_EVERDAY_AND_ANSWER_2_TIMES

        self.assertEqual(actual_result, expected_result)

    def test_answer_two_times(self):
        actual_result: str = Question(
            "2 times a week"
        ).get_how_often_do_you_wash_your_hair_answer()

        expected_result: str = TestTexts.ANSWER_EVERDAY_AND_ANSWER_2_TIMES

        self.assertEqual(actual_result, expected_result)

    def test_answer_one_time(self):
        actual_result: str = Question(
            "1 time a week"
        ).get_how_often_do_you_wash_your_hair_answer()

        expected_result: str = TestTexts.ANSWER_1_TIME_AND_ANSWER_3_TIMES

        self.assertEqual(actual_result, expected_result)

    def test_answer_three_times(self):
        actual_result: str = Question(
            "3 times a week"
        ).get_how_often_do_you_wash_your_hair_answer()

        expected_result: str = TestTexts.ANSWER_1_TIME_AND_ANSWER_3_TIMES

        self.assertEqual(actual_result, expected_result)
