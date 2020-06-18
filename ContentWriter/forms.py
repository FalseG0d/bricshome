from django.forms import ModelForm
from Home.models import Report

class ReportForm(ModelForm):
    class Meta:
        model=Report
        fields=['name','title','abstract','complete','pdf','thumbnail','image']