from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveSmallIntegerField()
    date_born = models.DateField()

    REQUIRED_FIELDS = ['email', 'age', 'date_born']

    def __str__(self) -> str:
        return self.username


class EmployerUser(CustomUser):
    pass


class CustomerUser(CustomUser):
    pass
