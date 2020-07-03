from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
        'phone', 'com']

class ContactForm(forms.Form):
    name=forms.CharField(label="Имя",widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label="Тема", widget=forms.TextInput(attrs={'class': 'form-control'}))
    message=forms.CharField(label="Текст",widget=forms.Textarea(attrs={'class':'form-control'}))