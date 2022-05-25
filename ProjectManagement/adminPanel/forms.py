from django import forms
from django.core.exceptions import ObjectDoesNotExist
from posts.models import Category
from adminPanel.models import AdminMessage
from home.models import QuestionAnswer

class Categoryform(forms.ModelForm):
    class Meta():
        model = Category
        fields = ['name',]

    def clean_name(self):
        data = self.cleaned_data['name']
        try:
            c = Category.objects.get(name=data)
            if c:
                raise forms.ValidationError("This category allready exists")
        except ObjectDoesNotExist:
            return data


class Q_A_form(forms.ModelForm):
    Question = forms.CharField(widget=forms.Textarea(
        attrs={
            'dir': 'rtl',
            'rows': 3,
            'cols': 40,
            'style': 'height: 6em; resize:none;',
        }
    ))

    Answer = forms.CharField(widget=forms.Textarea(
        attrs={
            'dir': 'rtl',
            'rows': 3,
            'cols': 40,
            'style': 'height: 6em; resize:none;',
        }
    ))

    class Meta():
        model = QuestionAnswer
        fields = ['Question','Answer']

        labels = {
            "Question":'שאלה',
            "Answer":'תשובה',
        }

class AdminMessageForm(forms.ModelForm):

    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'dir': 'rtl',
            'rows': 3,
            'cols': 40,
            'style': 'height: 6em; resize:none;',
        }
    ))
    class Meta():
        model = AdminMessage
        fields = ['content']

        labels = {
            "content":'תוכן',
        }
