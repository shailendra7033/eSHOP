from django import forms
from .models import Customer

class AddressForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','locality','city','state','pincode']
        widgets= {'name':forms.TextInput(attrs={'class':'form-control'}),
        'locality':forms.TextInput(attrs={'class':'form-control'}),
        'city':forms.TextInput(attrs={'class':'form-control'}),
        'state':forms.TextInput(attrs={'class':'form-control'}),
        'pincode':forms.NumberInput(attrs={'class':'form-control'})
        }
