from django.contrib.auth.models import User
from django.db import models


class Household(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    household = models.ForeignKey(
        Household,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class MonthlyBudget(models.Model):
    label = models.CharField(max_length=255, default="")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
