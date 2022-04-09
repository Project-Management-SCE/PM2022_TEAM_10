from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User , associationManager
from django.db import transaction

class AssociationManagerSignUpform(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    association_number = forms.CharField(required=True)
    email = forms.EmailField(max_length=100)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email' , 'phone_number', 'association_number')

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
        user.save()

        assoManager = associationManager.objects.create(user=user)
        assoManager.association_number = self.cleaned_data.get('association_number')

        assoManager.save()
        return user