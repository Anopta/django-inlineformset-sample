from django import forms
from .models import AppPost, AppItem


class ManagerAppForm(forms.Form):
    title = forms.CharField(max_length=255, label='説明書名')
    # item = forms.CharField(max_length=255, label='質問項目追加')


ManagerAppFormset = forms.inlineformset_factory(
    AppPost, AppItem, fields='__all__',
    extra=0, can_delete=False
)