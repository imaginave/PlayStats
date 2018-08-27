# Create your views here.

#from django.shortcuts import render
from django.http import HttpResponse
from .models import Transactions, News
from .tables import TransactionsTable
from .forms import TransactionsListFormHelper
from .utils import PagedFilteredTableView
from .filters import TransactionsListFilter
from .resources import TransactionResource
from django_tables2 import RequestConfig
from tablib import Dataset
from django.contrib.auth.models import User
from django_tables2 import MultiTableMixin
from django.views.generic.base import TemplateView

class TransactionsList(PagedFilteredTableView):
    model = Transactions
    table_class = TransactionsTable
    table_pagination = False
    filter_class = TransactionsListFilter
    formhelper_class = TransactionsListFormHelper
    template_name = 'stats/transactions_list.html'

    def get_context_data(self, **kwargs):
        context = super(TransactionsList, self).get_context_data(**kwargs)
        print(context['table'])
        context['news'] = News.objects.all()
        return context

    def post(self, *args, **kwargs ):
        if 'export_transactions' in self.request.POST:
            dataset = TransactionResource().export(self.get_queryset())
            response = HttpResponse(dataset.csv, content_type="csv")
            response['Content-Disposition'] = 'attachment; filename=filename.csv'
            return response


'''class TransactionsExport(View):

    def get(self, *args, **kwargs ):
        dataset = TransactionResource().export()
        response = HttpResponse(dataset.csv, content_type="csv")
        response['Content-Disposition'] = 'attachment; filename=filename.csv'
        return response'''

