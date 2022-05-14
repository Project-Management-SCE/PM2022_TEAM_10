from django import forms
from feedbacks.models import Feedback

class FeedbackFrom(forms.ModelForm):
    
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'dir': 'rtl',
        }
    ))
    
    class Meta():
        model = Feedback
        fields = ['subject','content',]
    
        labels = {
            "content":'תוכן',
            "subject":'נושא',
        }