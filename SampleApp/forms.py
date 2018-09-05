from django import forms

from .models import SampleModel, Entry


class SampleModelForm(forms.ModelForm):
    class Meta:
        model = SampleModel
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

