from django import forms
from models import Item
from django.contrib.auth.models import User

#class NewItemForm(forms.Form):
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item 
        fields = (
            'description',
            'price', 
        )
    #price = forms.IntegerField()
    #description = forms.CharField(max_length=200)

#class NewItemForm(forms.ModelForm):
#    class Meta:
#        model = User

class WhichSellerForm(forms.Form):
    seller = forms.ModelChoiceField(
        queryset=User.objects.all()
    )
