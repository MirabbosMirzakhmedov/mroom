import unittest

from mroom.report.tests.test_data.question_texts import TestTest


class Test_Question_3(unittest.TestCase):

    def test_question_3_DANDRUFF(self):
        # actual_result: str = Question(
        #     "Dandruff"
        # ).get_what_kind_of_problems_do_you_have_answer()
        
        expected_result: str = TestTest.QUESTION_3_ANSWER_1

        self.assertEqual(actual_result, expected_result)

    # DANDRUFF = "Dandruff"
    # HAIR_LOSS = "Hair loss"
    # DRY_HAIR = "Dry hair"
    # PSORIASIS = "Psoriasis"
    # HEAD_LICE = "Head lice"
    # BAMBOO_HAIR = "Bamboo hair"
    # VERY_OILY_HAIR = "Very oily hair"
