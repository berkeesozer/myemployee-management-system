from django.db import models
from datetime import date

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    birth_date = models.DateField(default=date.today)
    start_date = models.DateField(default=date.today)
    home_address = models.CharField(max_length=100, default='')
    mailing_address = models.CharField(max_length=100, default='')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

class Admin(models.Model):
    username = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=100, default='')


    def __str__(self):
        return f"{self.first_name} {self.last_name}"