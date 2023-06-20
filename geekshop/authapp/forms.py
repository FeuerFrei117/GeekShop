from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from authapp.validator import validate_name, validate_age
from authapp.models import User


class UserLoginForm(AuthenticationForm) :
    username = forms.CharField(widget=forms.TextInput(), validators=[validate_name])

    class Meta :
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs) :
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'
        for field_name, field in self.fields.items() :
            field.widget.attrs['class'] = 'form-control py-4'

    # def clean_username(self):
    #     data = self.cleaned_data['username']
    #     if not data.isalpha():
    #         raise ValidationError(_(f'Имя пользователя не может содержать цифры'), params={'value': data},)
    #     return data


class UserRegisterForm(UserCreationForm) :
    class Meta :
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs) :
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите адрес эл.почты'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
        for field_name, field in self.fields.items() :
            field.widget.attrs['class'] = 'form-control py-4'


class UserProfileForm(UserChangeForm) :
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    age = forms.IntegerField(widget=forms.NumberInput(), required=False, validators=[validate_age])

    class Meta :
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'image', 'age']

    def __init__(self, *args, **kwargs) :
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True

        for field_name, field in self.fields.items() :
            field.widget.attrs['class'] = 'form-control py-4'

        self.fields['image'].widget.attrs['class'] = 'custom-file-input'
