from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text','recommend',)
        labels = {'text': 'متن نظر شما'}
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control rounded-3',
                'rows': 5,
                'placeholder': 'نظر خود را بنویسید...',
                'dir': 'rtl',
            })
        }
