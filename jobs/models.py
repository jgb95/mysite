from django.db import models
from datetime import datetime


class Company(models.Model):
    name = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Companies'


class Job(models.Model):
    title = models.CharField(max_length=200)
    job_description = models.TextField()
    date_posted = models.DateTimeField(default=datetime.now)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " - " + self.company.name


class User(models.Model):
    name = models.CharField(max_length=200)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
