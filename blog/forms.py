from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment ,Post,Tag

class CommentForm(forms.ModelForm):
    text=forms.Textarea()
    class Meta:
        model=Comment
        exclude=['post' ,'username','is_approved']
        labels={
            'email':'your email',
            'text':'your comment'

        }
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            
            self.fields['text'].widget.attrs.update({'class':"form-control mr-sm-2", 'rows':"5" ,'id':"comment"})
        
        # widget={'text':forms.Textarea(attrs={ 'class':'form-control', 'rows':"5" ,'id':"comment" }),
        #           'email':forms.TextInput(attrs={'class':'form-control'  })                    

        # }

class UserForm(UserCreationForm):
    email=forms.EmailField()
    username=forms.CharField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']



class WritePostForm(forms.ModelForm):
    tags=forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                        widget=forms.CheckboxSelectMultiple)
   
    class Meta:
        model=Post
        fields=["title",'excerpt','image','content','category','tags']
        

class SearchForm(forms.Form):
    query=forms.CharField()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['query'].label=''
        self.fields['query'].widget.attrs.update({'class':"form-control mr-sm-2"})
    

















# class UserForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['username','first_name','last_name','email','password']
