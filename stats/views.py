# Create your views here.

from django.shortcuts import  render
from .models import Transations
from .tables import TransactionsTable
from django_tables2 import RequestConfig
from django.contrib.auth.decorators import login_required
from tablib import Dataset
from .resources import TransactionResource



@login_required
def transactions(request):
    table = TransactionsTable(Transations.objects.filter(Nickname = request.user))
    RequestConfig(request).configure(table)
    return render(request, 'stats/transactions.html', {'transations': table})

@login_required
def simple_upload(request):
    if request.method == 'POST':
        transaction_resource = TransactionResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = transaction_resource.import_data(dataset, dry_run=True)  # Test the data import
        print(imported_data)
        if not result.has_errors():
            transaction_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'stats/import.html')
