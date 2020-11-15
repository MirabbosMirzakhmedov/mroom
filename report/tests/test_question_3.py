import unittest

from report.questions import Question
from report.tests.test_data.question_texts import TestTest


class TestQuestionThree(unittest.TestCase):

    def test_answer_1(self):
        actual_result: str = Question(
            ["Dandruff",
             "Dry hair",
             "Psoriasis"]
        ).get_what_kind_of_problems_do_you_have_answer()

        expected_result: str = TestTest.QUESTION_3_ANSWER_1

        self.assertEqual(actual_result, expected_result)

    def test_answer_2(self):
        actual_result: str = Question(
            ["Head lice",
             "Psoriasis"]
        ).get_what_kind_of_problems_do_you_have_answer()

        expected_result: str = TestTest.QUESTION_3_ANSWER_2

        self.assertEqual(actual_result, expected_result)

    def test_answer_3(self):
        actual_result: str = Question(
            ["Very oily hair",
             "Dry hair",
             "Dandruff"]
        ).get_what_kind_of_problems_do_you_have_answer()

        expected_result: str = TestTest.QUESTION_3_ANSWER_3

        self.assertEqual(actual_result, expected_result)

    def test_answer_4(self):
        actual_result = Question(
            ["Bamboo hair"]
        ).get_what_kind_of_problems_do_you_have_answer()

        expected_result: str = TestTest.QUESTION_3_ANSWER_3_else

        self.assertEqual(actual_result, expected_result)


