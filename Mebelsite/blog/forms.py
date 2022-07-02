from django import forms

from blog.models import Mebelforma


class MebelForm(forms.ModelForm):
    class Meta:
        model = Mebelforma
        fields = '__all__'