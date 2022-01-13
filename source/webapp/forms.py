from django import forms
# from django.forms import widgets
from django.forms import ModelForm

from webapp.models import Type, Status, IssueTracker


class IssueTrackerForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label="Краткое описание")
    description = forms.CharField(max_length=200, required=True, label="Полное описание")
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label="Статус")
    type = forms.ModelChoiceField(queryset=Type.objects.all(), label="Тип")
    # class Meta:
    #     model = IssueTracker
    #     fields = '__all__'
