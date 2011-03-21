from django import forms
from models import Item

#class NewItemForm(forms.Form):
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
    #price = forms.IntegerField()
    #description = forms.CharField(max_length=200)

#class NewItemForm(forms.ModelForm):
#    class Meta:
#        model = User
