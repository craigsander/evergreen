from django.shortcuts import render

# Create your views here.

textfield = {
	'input_type':'textarea',
	'required':0,
	}
	
charfield = {
	'input_type':'text',
	}

datefield = {
	'input_type':'text',
	'classes': ['datepicker',]

	}

'''
The goal here is to create a way of dealing with added fields. 

For example: 

Let's say we have a page object that needs an 'Introduction' section. I want the developer to be able to ....


Whoa, whoa, whoa. I'm just realizing that my thought of having quickly addable fields 


class JSONFieldForm():
	
	
	
	
	
	return None

def text_field():
	return None
	
def date_field():
	return None
	
def datetime_field():
	return None
	
def 
