
# Register your models here.

from django.contrib import admin
from .models import Transactions,Account,Agent,News
from import_export.admin import ImportExportModelAdmin

@admin.register(Account)
class AccountAdmin(ImportExportModelAdmin):
    list_display = ('id','name', 'player', 'phone', 'agent')
    #inlines = [TransactionsInline]
    pass

@admin.register(Agent)
class Agent(ImportExportModelAdmin):
    pass

@admin.register(Transactions)
class TransactionsAdmin(ImportExportModelAdmin):
    list_display = ('id','name','date','results','after_rake','win','turnover')
    list_filter = ('name', 'date')

#class TransactionsAdmin(ImportExportModelAdmin):
#    pass

@admin.register(News)
class News(ImportExportModelAdmin):
    pass

