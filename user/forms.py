from django.forms import ModelForm

from .models import User, Profile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField


class MyAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(MyAuthenticationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input'


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['country', 'city', 'image']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input'
