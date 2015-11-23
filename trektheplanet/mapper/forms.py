from django import forms


	
class contact(forms.Form):
	pass 



class ExpForm(forms.Form):
	host = forms.CharField(max_length=25, required=True) 
	address = forms.CharField(max_length=100, required=True)
	country = forms.CharField(max_length=25, required=True) 
	#contact  = forms.ForeignKey(contact)
	
