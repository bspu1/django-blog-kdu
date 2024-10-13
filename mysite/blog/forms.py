from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше ім\'я'}),
            'body': forms.Textarea( attrs={'placeholder': 'Ваш коментар', 'rows': 4}),
        }
        labels = {
            'name': 'Ім\'я',
            'body': 'Коментар'
        }
