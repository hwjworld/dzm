from django import forms
from django.forms.extras.widgets import SelectDateWidget

class RecordForm(forms.Form):
    visit_date = forms.CharField(label='日期', max_length=10, initial='today')
    street = forms.CharField(label='胡同(街)', max_length=100)
    num = forms.CharField(label='门牌', max_length=100)
    response = forms.CharField(label='反应', max_length=100)
    volunteer = forms.CharField(label='义工', max_length=100)

