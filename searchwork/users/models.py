from django.db import models
from django.contrib.auth.models import AbstractUser


class City(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name


class CustomUser(AbstractUser):
    city = models.ForeignKey('City', on_delete=models.PROTECT,
                             related_name='user_city')
    age = models.PositiveSmallIntegerField()
    date_born = models.DateField()

    def __str__(self) -> str:
        return self.username


class EmployerUser(CustomUser):
    pass


class CustomerUser(CustomUser):
    pass
