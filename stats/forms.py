from django import forms
from .models import Transactions
from crispy_forms.helper import FormHelper


class TransactionsListFormHelper(FormHelper):
    model = Transactions
    form_tag = False