from django.db import models
from mroom.api.models import (
    ProjectModel,
    User
)


class Answer(ProjectModel):
    VERY_SHORT = 'very_short'
    SHORT = 'short'
    MEDIUM = 'medium'
    LONG = 'long'

    EVERYDAY = 'everyday'
    TWO_TIMES = 'two_times'
    ONE_TIME = 'one_time'
    THREE_TIMES = 'three_times'

    DANDRUFF = 'dandruff'
    HAIR_LOSS = 'hair_loss'
    DRY_HAIR = 'dry_hair'
    PSORIASIS = 'psoriasis'
    HEAD_LICE = 'head_lice'
    BAMBOO_HAIR = 'bamboo_hair'
    VERY_OILY_HAIR = 'very_oily'

    EUR = 'eur'
    USD = 'usd'

    price_120 = 120
    price_265 = 265
    price_60 = 60
    price_132 = 132

    CHOICE_YES = 'yes'
    CHOICE_YES_ALOE_LIQUID = 'aloe_liquid'
    CHOICE_YES_LEMON = 'lemon'
    CHOICE_YES_GARLIC = 'garlic_water'
    CHOICE_YES_NOT_WASHING = 'not_washing'

    CHOICE_I_DONT_KNOW = "idk"

    CHOICE_NO = 'no'


    KEYS = (
        (VERY_SHORT, 'Very short'),
        (EVERYDAY, 'Everyday'),
        (DANDRUFF, 'Dandruff'),
        (HAIR_LOSS, 'Hair loss'),
        (DRY_HAIR, 'Dry hair'),
        (PSORIASIS, 'Psoriasis'),
        (HEAD_LICE, 'Head lice'),
        (BAMBOO_HAIR, 'Bamboo hair'),
        (VERY_OILY_HAIR, 'Very oily hair'),
        (EUR, 'EUR'),
        (USD, 'USD'),
        (CHOICE_I_DONT_KNOW, "I don't know"),
        (CHOICE_NO, 'No'),
        (CHOICE_YES, 'Yes'),
        (CHOICE_YES_ALOE_LIQUID, 'Applying aloe liquid'),
        (CHOICE_YES_LEMON, 'Applying lemon'),
        (CHOICE_YES_GARLIC, 'Applying garlic water'),
        (CHOICE_YES_NOT_WASHING, 'Do not washing')
    )

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    key = models.CharField(choices=KEYS, max_length=128)


class Question(ProjectModel):
    name = models.CharField(max_length=255)
    answers = models.ManyToManyField(
        to=Answer,
        related_name='questions',
    )
    solutions = models.ManyToManyField(
        to=Answer,
        related_name='questions_set',
    )




class Survey(ProjectModel):
    DEFAULT = 'default'

    KEYS = (
        (DEFAULT, 'Default survey'),
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='surveys',
        null=True
    )
    questions = models.ManyToManyField(
        to=Question,
        related_name='surveys',
    )

    key = models.CharField(choices=KEYS, max_length=255)