from django import forms
from django_countries.fields import LazyTypedChoiceField
from django_countries import countries
from django_countries.widgets import CountrySelectWidget
from phonenumber_field.formfields import PhoneNumberField

	
class contact(forms.Form):
	pass 



class ExpForm(forms.Form):
	contact_preference = (
		('phone','phone'),
		('email','email'),
		('mail','mail'),
	)
	host = forms.CharField(max_length=25, required=True) 
	preference = forms.ChoiceField(choices=contact_preference, required=True) 
	#contact = forms.CharField(max_length=25, required=True) 
	email = forms.EmailField(required=False)
	phone = PhoneNumberField(required=False)
	address = forms.CharField(max_length=100, required=True)
	country = LazyTypedChoiceField(choices=countries, widget= CountrySelectWidget())
	#preferred method of contact
	#contact  = forms.ForeignKey(contact)
	
