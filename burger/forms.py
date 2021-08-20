from .models import getInTouch
from django.forms import ModelForm, TextInput, Textarea


class getInTouchForm(ModelForm):
    class Meta:
        model = getInTouch
        fields = ['message', 'name', 'email', 'subject']
        widgets = {
            "subject": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название Темы: '
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя: '
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш почтовый адрес: '
            }),
            "message": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше сообщение: '
            }),

        }
