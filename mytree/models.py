import datetime

from django.db import models
from utils.models import AbstractLayer


class Job(AbstractLayer):
    """Jobs list in the Company"""
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Subdivision(AbstractLayer):
    title = models.CharField(max_length=200)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return self.title


class Employee(AbstractLayer):
    """Employees of Company"""
    name = models.CharField(max_length=200)
    job_title = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    employment_date = models.DateTimeField(default=datetime.datetime.now)
    salary = models.FloatField(null=True)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
