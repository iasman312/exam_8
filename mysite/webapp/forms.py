from django import forms
from django.contrib.auth import get_user_model

from webapp.models import Product, Feedback


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'picture')


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        user = get_user_model()
        fields = ('feedback_text', 'rating')


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')