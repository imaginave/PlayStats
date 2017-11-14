from import_export import resources

from stats.models import Transations


class TransactionResource(resources.ModelResource,):

    class Meta:
        model = Transations
        #exclude = ('Name',)

