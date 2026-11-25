from django import forms
from .models import Job

class Jobform(forms.ModelForm):
  class Meta:
    model = Job
    fields= ['title','c_name','description','location','salary']

    
    
