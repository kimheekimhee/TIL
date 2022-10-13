# accounts/models.py

"""
(보너스) 한국이름 풀네임으로 나오게 커스텀하기
"""

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"
