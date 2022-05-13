from django.contrib.auth.forms import UserCreationForm
from django import forms

from associations.models import Association
from .models import User , associationManager, HelpoUser
from django.db import transaction

from django.core.exceptions import ObjectDoesNotExist


class AssociationManagerSignUpform(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    association_number = forms.CharField(required=True)
    email = forms.EmailField(max_length=100)
    high_privacy =forms.BooleanField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email' , 'phone_number', 'association_number','password1','password2','high_privacy')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_association_manager = True
        user.is_active = False
        user.username = self.cleaned_data.get('username')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.high_privacy = self.cleaned_data.get('high_privacy')
        user.save()

        assoManager = associationManager.objects.create(user=user)
        assoManager.association_number = self.cleaned_data.get('association_number')

        assoManager.save()
        return user

    def clean_association_number(self):
        data = self.cleaned_data['association_number']
        try:
            assos = Association.objects.get(id=data)
            if assos.manager:
                raise forms.ValidationError("This association allready got a manager")
        except ObjectDoesNotExist as e:
            raise forms.ValidationError("Unknown association number. Enter a valid number")
        return data

    
    
    
class HelpoUserSignUpform(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    city = forms.CharField(required=True)
    email = forms.EmailField(max_length=100)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email' , 'phone_number', 'city')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_association_manager = False
        user.is_helpo_user=True
        user.is_active = True
        user.username = self.cleaned_data.get('username')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.save()

        helpoUser = HelpoUser.objects.create(user=user)
        helpoUser.city = self.cleaned_data.get('city')

        helpoUser.save()
        return user
    
    

class UserUpdateform(forms.ModelForm):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email' , 'phone_number', 'high_privacy')



class AssociationManagerUpdateform(forms.ModelForm):
    association_number = forms.CharField(required=True)
    
    class Meta(UserCreationForm.Meta):
        model = associationManager
        fields = ( 'association_number',)
    
    
class HelpoUserUpdateform(forms.ModelForm):
    
    class Meta(UserCreationForm.Meta):
        model = HelpoUser
        fields = ( 'city',)

class UserBlockForm(forms.ModelForm):
    blocked_reason = forms.CharField(widget=forms.Textarea(
        attrs={
            'dir': 'rtl',
        }
    ))
    class Meta:
        model = User
        fields = [ 'blocked_reason',]
        
        labels = {
            'blocked_reason':'סיבה',
        }