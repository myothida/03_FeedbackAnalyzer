from django import forms
from .model import feedback

class feedbackForm(forms.ModelForm):
    class Meta:
              model = feedback
              fields = "__all__"

    language = forms.TypedChoiceField(choices=[('Eng','English'),('Burmese', 'Burmese')],
                                      initial='Eng')
    text = forms.CharField(max_length=10000, label="" ,
                               widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}))
    