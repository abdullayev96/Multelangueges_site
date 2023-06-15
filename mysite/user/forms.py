from django import  forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models  import User



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:

        model = User
        fields = [
            'username', 'first_name',
            'last_name', 'email',
            'password1', 'password2'
        ]

# class LoginUserForm(AuthenticationForm):
#     username = forms.CharField (label = 'Login' , widget = forms.TextInput(attrs = {'class' : 'form-input' } ) )
#     password = forms.CharField (label = 'Password' , widget = forms.PasswordInput(attrs = {'class' : 'form-input' } ) )

#
# class RegisterUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2')
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-input'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
#             'password2': forms.PasswordInput(attrs={'class':  'form -input' })
#         }