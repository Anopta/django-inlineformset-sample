from django import forms
from .models import AppPost, AppItem


class PostCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = AppPost
        fields = '__all__'


FileFormset = forms.inlineformset_factory(
    AppPost, AppItem, fields='__all__',
    extra=3, can_delete=False
)