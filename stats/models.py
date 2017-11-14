
# Create your models here.
from django.db import models


class Transations(models.Model):
    transaction_date = models.DateField
    Name = models.CharField(max_length=50)
    Table_no = models.CharField(max_length=50)
    Original_win_loss = models.DecimalField(max_digits=11, decimal_places=2,default=0)
    Final_win_loss = models.DecimalField(max_digits=11, decimal_places=2,default=0)
    Turnover = models.DecimalField(max_digits=11, decimal_places=2,default=0)
    Player = models.CharField(max_length=100,default='')
    Nickname = models.CharField(max_length=100,default='')


