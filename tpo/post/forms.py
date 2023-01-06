from django.forms import ModelForm, widgets
from django import forms
from post.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'description', 'price', 'image', 'publicationsDate'}
        ordering = ["-publicationsDate"]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder':'Titulo del producto'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder':'Descripcion'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder':'Precio'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'type': 'file', 'method': 'POST', 'placeholder':'Imagen'}),
            'publicationsDate': forms.DateInput(attrs={'class': 'form-control', 'placeholder':'Fecha', 'type': 'date'})
        }