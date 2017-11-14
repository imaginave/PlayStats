# tutorial/tables.py
import django_tables2 as tables

from stats.models import Transations


class TransactionsTable(tables.Table):
    class Meta:
        model = Transations
        template = 'django_tables2/bootstrap.html'