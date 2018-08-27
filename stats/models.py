# Create your models here.
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings

class Agent(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)

class Account(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50, blank=True)
    player = models.CharField(max_length=50,blank=True)
    phone = models.CharField(max_length=50,blank=True)
    user = models.ManyToManyField(User,default = 1)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, default=1)


class Transactions(models.Model):
    def __str__(self):
        return '%s %s' % (self.name, self.date)
    name = models.ForeignKey(Account, on_delete=models.CASCADE, default=1)
    date = models.DateField(default=datetime.now, blank=True)
    results = models.DecimalField(max_digits=11, decimal_places=2,default=0)
    after_rake = models.DecimalField(max_digits=11, decimal_places=2,default=0)
    win = models.DecimalField(max_digits=11, decimal_places=2,default=0)
    turnover = models.DecimalField(max_digits=11, decimal_places=2,default=0)
    class Meta:
        permissions = (
            ("can_upload", "Can upload"),
        )

class News(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100)
    txt = models.TextField()