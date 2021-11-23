from django import forms
from .models import Post, Vegan_type

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['date', 'food_name', 'content', 'post_vegan_type', 'image']
        label = {'date', 'food_name', 'content', 'post_vegan_type', 'image'}
