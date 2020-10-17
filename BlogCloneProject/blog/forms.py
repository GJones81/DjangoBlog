from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')
        #adds a CSS Class to the widget created from this object
        widgets = {
            'title': forms.TextInput(attrs = {'class': 'textinputclass'}),
            'text': forms.Textarea(attrs = {'class': 'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text',)
        #adds a CSS class to the widget created from this object
        widgets = {
            'author': forms.TextInput(attrs = {'class': 'textinputclass'}),
            'text': forms.Textarea(attrs = {'class': 'editable medium-editor-textarea'})
        }