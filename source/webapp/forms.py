from django import forms
# from django.forms import widgets
from django.forms import ModelForm

from webapp.models import Type, Status


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label="Краткое описание")
    description = forms.CharField(max_length=200, required=True, label="Полное описание")
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label="Статус")
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), required=False, label="Тип")