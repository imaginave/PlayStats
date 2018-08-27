from import_export import resources
from stats.models import Transactions

class TransactionResource(resources.ModelResource):
    class Meta:
        model = Transactions

