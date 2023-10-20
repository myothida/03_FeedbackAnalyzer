from django import forms
from .models import feedback

class feedbackForm(forms.ModelForm):
    class Meta:
              model = feedback
              fields = "__all__"

    language = forms.TypedChoiceField(choices=[('Eng','English'),('Burmese', 'Burmese')])
    text = forms.CharField(max_length=1000)
    