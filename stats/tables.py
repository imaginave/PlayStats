# tutorial/tables.py

import django_tables2 as tables
from .models import Transactions

class TransactionsTable(tables.Table):
    name = tables.Column(footer='Total:')
    results = tables.Column(footer=lambda table: sum(x.results for x in table.data))
    after_rake = tables.Column(footer=lambda table: sum(x.after_rake for x in table.data))
    win = tables.Column(footer=lambda table: sum(x.win for x in table.data))
    turnover = tables.Column(footer=lambda table: sum(x.turnover for x in table.data))

    class Meta:
        model = Transactions
        orderable = False
        row_attrs = {
            'name': lambda record: record.name,
            'display': 'hide'
        }
        attrs = {
            "class": "table",
        }
        exclude = {'id'}

