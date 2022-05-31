from pyexpat import model
from django import forms
from django.forms import fields, widgets
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','image','image_url','published','categories']
        widgets = {
            'title': forms.Textarea(attrs={'placeholder': 'Title..'}),
            'content': forms.Textarea(attrs={'placeholder': 'What is on your mind?'})
            
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {  
            'content': forms.Textarea(attrs={'placeholder': 'add a comment..'}),    
        }