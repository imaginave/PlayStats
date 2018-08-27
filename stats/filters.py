# filters.py
import django_filters
from django_filters import DateFromToRangeFilter
from django_filters.widgets import RangeWidget
from django import forms
from .models import Transactions,Account
from django.contrib.auth.models import User
from django.db.models import Q
from crum import get_current_user, get_current_request
from django_filters import filters
from datetime import date, timedelta


class TransactionsListFilter(django_filters.FilterSet):

    date = DateFromToRangeFilter(widget=RangeWidget(attrs={
                                                            'placeholder': 'MM/DD/YYYY',
                                                            'class': 'mydatepicker'
                                                           }))
    class Meta:
        model = Transactions
        fields = ['date']

    @property
    def qs(self):
        account_list = Account.objects.filter(user=get_current_user())
        account_filter_qs = Q()
        for name in account_list:
            account_filter_qs = account_filter_qs | Q(name=name)
        req = get_current_request()
        data = req.GET.copy()
        parent = super(TransactionsListFilter, self).qs
        if len(data) == 0: #initial filtering for today
            return parent.filter(account_filter_qs).filter(date__gte=date.today()-timedelta(1)).order_by('name')
        return parent.filter(account_filter_qs).order_by('name')


