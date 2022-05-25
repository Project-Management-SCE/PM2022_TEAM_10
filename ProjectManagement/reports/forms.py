from django import forms
from .models import PostReport,UserReport


INFO_CHOICES= [
    ('ספאם', 'ספאם'),
    ('לא תואם את מטרת האתר', 'לא תואם את מטרת האתר'),
    ('תוכן פוגעני', 'תוכן פוגעני'),
    ('משתמש בכוחו לרעה', 'משתמש בכוחו לרעה'),
    ]

class reportPostForm(forms.ModelForm):
    info = forms.CharField(label='בחר סיבת דיווח', widget=forms.Select(choices=INFO_CHOICES,
        attrs={
            'dir': 'rtl',
        }
        ))

    class Meta():
        model = PostReport
        fields = ['info',]

class reportUserForm(forms.ModelForm):
    reason = forms.CharField(widget=forms.Textarea(
        attrs={
            'dir': 'rtl',
        }
    ))

    class Meta():
        model = UserReport
        fields = ['reason',]
        