from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Users

class UserCategory(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Users
        fields = ('id', 'name', 'is_featured')

class UserChangeForm(UserChangeForm):

    class Meta:
        model = Users
        fields = UserChangeForm.Meta.fields