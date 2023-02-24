from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment 

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['post' ,'username']
        labels={
            'email':'your email',
            'text':'your comment'

        }

class UserForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']

# class UserForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['username','first_name','last_name','email','password']