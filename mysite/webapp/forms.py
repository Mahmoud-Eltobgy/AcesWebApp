from django import forms
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
