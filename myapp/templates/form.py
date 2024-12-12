from django import forms  
from myapp.models import Student  
  
class StdForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = "__all__"        