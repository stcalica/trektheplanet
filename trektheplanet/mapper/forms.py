from django import forms
from django_countries.fields import LazyTypedChoiceField
from django_countries import countries
from django_countries.widgets import CountrySelectWidget

	
class contact(forms.Form):
	pass 



class ExpForm(forms.Form):
	host = forms.CharField(max_length=25, required=True) 
	address = forms.CharField(max_length=100, required=True)
	country = LazyTypedChoiceField(choices=countries, widget= CountrySelectWidget())

	#contact  = forms.ForeignKey(contact)
	
