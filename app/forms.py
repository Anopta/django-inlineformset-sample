from django import forms
from .models import Post, File


class PostCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Post
        fields = '__all__'


FileFormset = forms.inlineformset_factory(
    Post, File, fields='__all__',
    extra=5, max_num=5, can_delete=False
)