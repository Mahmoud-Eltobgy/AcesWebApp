from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,get_user_model

User = get_user_model()
class UserLoginForm(forms.Form):
    Email=forms.CharField()
    Password=forms.CharField(widget=forms.PasswordInput)
    def clean(self, *args, **kwargs):
        Email = self.cleaned_data.get("Email")
        Password = self.cleaned_data.get("Password")
        if Email and Password :
            user = authenticate(username= Email ,password=Password)
            if not user:
                raise forms.ValidationError("This user dosen't Exist")
            if not user.check_password(Password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
               raise forms.ValidationError("The user is no longer active try to login again")
        return super(UserLoginForm,self).clean(*args,**kwargs)



class RegisterationForm(forms.ModelForm):
    first_name=forms.CharField(required=True)
    password=forms.CharField(widget=forms.PasswordInput)
    password_Again=forms.CharField(widget=forms.PasswordInput)
    #Phone=forms.IntegerField()
    class Meta:
        model=User
        fields=[
        'username',
        'password',
        'password_Again',
        'first_name',
        ]


    def __init__(self, *args, **kwargs):
        super(RegisterationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Your Email:"
        self.fields['first_name'].label = "Your Phone:"
    def clean_password_Again(self):
        password = self.cleaned_data.get('password')
        password_Again = self.cleaned_data.get('password_Again')
        print(password)
        print(password_Again)
        if password != password_Again:
            raise forms.ValidationError('passwords Mismatch')

        return password
