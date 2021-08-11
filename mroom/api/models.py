import uuid

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models

from mroom.common.utils import gen_session_token


class TimestampModel(models.Model):
    class Meta:
        abstract = True

    created_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(auto_now=True)


class ProjectModel(TimestampModel):
    class Meta:
        abstract = True

    uid = models.UUIDField(unique=True, null=False, default=uuid.uuid4)


class UserManager(BaseUserManager):
    def create_user(
            self,
            email,
            name,
            terms,
            password=None,
    ):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            terms=terms,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, ProjectModel):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, null=False, default=str)
    terms = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []


class Session(ProjectModel):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='sessions'
    )
    token = models.TextField(default=gen_session_token, unique=True)
    last_active = models.DateTimeField(auto_now_add=True, db_index=True)
