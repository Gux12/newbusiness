# -*- coding:utf-8 -*-
from django import forms

class UserForm(forms.Form):
    FirstName = forms.CharField(label='名字',max_length=50)
    LastName = forms.CharField(label='姓氏',max_length=50)
    Instrument = forms.CharField(label='乐器',max_length=50)