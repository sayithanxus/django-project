from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput

from user.models import UserProfile


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30,label= 'Kullanıcı adı :')
    email = forms.EmailField(max_length=200,label= 'E-posta :')
    first_name = forms.CharField(max_length=100, help_text='Ad',label= 'Ad :')
    last_name = forms.CharField(max_length=100, help_text='Soyad',label= 'Soyad :')

    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password1', 'password2', )

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ( 'username','email','first_name','last_name')
        widgets = {
            'username'  : TextInput(attrs={'class': 'input','placeholder':'Kullanıcı adı'}),
            'email'     : EmailInput(attrs={'class': 'input','placeholder':'E-posta'}),
            'first_name': TextInput(attrs={'class': 'input','placeholder':'Ad'}),
            'last_name' : TextInput(attrs={'class': 'input','placeholder':'Soyad' }),
        }

CITY = [
    ('Istanbul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Izmir', 'Izmir'),
]
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city','country','image','language')
        widgets = {
            'phone'     : TextInput(attrs={'class': 'input','placeholder':'phone'}),
            'address'   : TextInput(attrs={'class': 'input','placeholder':'address'}),
            'city'      : Select(attrs={'class': 'input','placeholder':'city'},choices=CITY),
            'country'   : TextInput(attrs={'class': 'input','placeholder':'country' }),
            'image'     : FileInput(attrs={'class': 'input', 'placeholder': 'image', }),
        }