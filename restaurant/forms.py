from django.forms import ModelForm
from restaurant.models import *
from django import forms

class FormUser(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput({'class': 'form-control'}),
            'username': forms.TextInput({'class': 'form-control'}),
            'email': forms.EmailInput({'class': 'form-control'}),
            'password': forms.PasswordInput({'class': 'form-control'}),
        }
        
class FormTable(ModelForm):
    class Meta:
        model = Table
        fields = '__all__'
        
        widgets = {
            'table_number': forms.TextInput({'class': 'form-control'}),
            'table_capacity': forms.NumberInput({'class': 'form-control'}),
            'table_status': forms.TextInput({'class': 'form-control'}),
        }
        
class FormMenu(ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        
        widgets = {
            'menu_name': forms.TextInput({'class': 'form-control'}),
            'menu_description': forms.Textarea({'class': 'form-control'}),
            'menu_price': forms.NumberInput({'class': 'form-control'}),
        }
        
class FormFormula(ModelForm):
    class Meta:
        model = Formula
        fields = '__all__'
        
        widgets = {
            'menu_id': forms.Select({'class': 'form-control'}),
            'description': forms.Textarea({'class': 'form-control'}),
            'ingredient': forms.Textarea({'class': 'form-control'}),
            'directive': forms.Textarea({'class': 'form-control'}),
        }
        
class FormOrder(ModelForm):
    class Meta:
        model = Order

        exclude =['grand_total']
        widgets = {
            'table_id': forms.Select({'class': 'form-control'}),
            'menu_id': forms.Select({'class': 'form-control'}),
            'order_date': forms.TextInput({'class': 'form-control'}),
            'payment_method': forms.TextInput({'class': 'form-control'}),
            'order_status': forms.TextInput({'class': 'form-control'}),
        }