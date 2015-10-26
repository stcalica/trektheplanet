from django import forms


	
class contact(forms.Form):
	pass 



class ExpForm(forms.Form):
	host = forms.CharField(max_length=25) 
	address = forms.CharField(max_length=100)
	country = forms.CharField(max_length=25) 
	#contact  = forms.ForeignKey(contact)
	
