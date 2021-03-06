import json


""" 

The goal here is to create a JSON-style validation model for common form inputs, similar to what Django does with it's models.Model.

At first we simply need to create a basic model with some basic attributes that can autopopulate JSONFields with the proper model. For now, this is to build the form element on the user end for dynamic forms.

We will later need to add some verification methods, again, similar to what Django does in Python.


Thinking out loud. 

Okay, so we need to allow custom fields to each of the models with jsonfields. 

In the 'type' model, we declare what types of data we want to make available. 

In the object itself, we want to fill out the data for those fields. 

So, in the type we declare the basic settings of the form. 

In the object, we collect the data for that form. 

So, we need some choices 


http://codepen.io/travist/full/xVyMjo/

Checkout form.io. It's exactly what you're discussing. It's the same thing. 

Things I really like:
- Multiple - like SheepIt (http://stackoverflow.com/questions/34532871/add-multiple-fields-to-form)
- Plugins to handle drag-and-drop files, etc.

{"test": "true", "list": ["test1", "test2", "test3"]}

"""


#
# There is a tremendous amount of stuff in django.db.models.fields which could/should be applied to validating and creating these JSON models, however,
# for the sake of getting a working system in place as quickly as possible, that will have to wait. 
#
# For now, the minimum viable product must suffice.
#



# There's the json-field models. They define what each field type should have

# there's the parent-settings object, which outlines the fields. there, the admin/developer will change the add json variables to the dict. The developer will then write the values to the necessary fields (hidden, required, multiple, etc).

# On the creation of each child object, the schema will display the forms accordingly. 

# on save, the schema, with the submitted form values, will be saved to the JSON data field. 

# How does the system know what input type to create? What does django forms do? 

def merge_two_dicts(x, y):
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z



__all__ = [str(x) for x in (
    'BooleanField', 'CharField','DateField', 'DateTimeField', 'DecimalField',
    'EmailField', 'FilePathField', 'PositiveIntegerField','PositiveSmallIntegerField', 'SlugField', 'SmallIntegerField', 'TextField',
    'TimeField', 'URLField', 'UUIDField', 'ImagePathField',
)]


__base_field_data__ = {
	'label':'',
	'inputMask':'',
	'placeholder':'',
	'value':'',
	'displayValue':'',
	'multiple':'',
	'helpText':'',
	'prefix':'',
	'suffix':'',
	'id':'',
	'classes':[],
	'customTemplate':'',
}

class JSONCharField(args=None):
	name = 'String Field'
	base = __base_field_data__
	custom_fields = {
		'inputType':'text',
		'hidden':'',
		'multiple':'',
		'unique':'',
		'validation': {
			"required":"",
			"minLength":"",
			"maxLength":"",
			"pattern":"",
			"custom":"",
			"customPrivate":"",			
		},	
	}
	
	def validate(self):
		# check max/min length
		# check pattern? 
		# check required
		return None
		
	def compiled(self):
		return merge_two_dicts(self.base, self.custom_fields)


class JSONEmailField():
	name = 'Email Field'
	base = __base_field_data__
	custom_fields = {}
	
	def validate(self):
		return None
		
	def compiled(self):
		return merge_two_dicts(self.base, self.custom_fields)

class JSONBooleanField():
	name = 'Boolean Field'
	base = __base_field_data__
	custom_fields = {}
	
	def validate(self):
		return None
		
	def compiled(self):
		return merge_two_dicts(self.base, self.custom_fields)


class JSONDateField():
	name = 'Date Field'	
	base = __base_field_data__
	custom_fields = {}
	
	def validate(self):
		return None
		
	def compiled(self):
		return merge_two_dicts(self.base, self.custom_fields)

class JSONDateTimeField():
	name = 'Datetime Field'	
	base = __base_field_data__
	custom_fields = {}
	
	def validate(self):
		return None
		
	def compiled(self):
		return merge_two_dicts(self.base, self.custom_fields)


class JSONFilePathField():
	name = 'File Field'	
	base = __base_field_data__
	custom_fields = {}
	
	def validate(self):
		return None
		
	def compiled(self):
		return merge_two_dicts(self.base, self.custom_fields)


class JSONIntegerField():
	name = 'Integer Field'	
	base = __base_field_data__
	custom_fields = {}
	
	def validate(self):
		return None
		
	def compiled(self):
		return merge_two_dicts(self.base, self.custom_fields)


class JSONDecimalField():
	name = 'Decimal Field'	
	base = __base_field_data__
	custom_fields = {}
	
	def validate(self):
		return None
		
	def compiled(self):
		return merge_two_dicts(self.base, self.custom_fields)

class JSONImageField():
	name = 'Image Field'	
	base = __base_field_data__
	custom_fields = {}
	
	def validate(self):
		return None
		
	def compiled(self):
		return merge_two_dicts(self.base, self.custom_fields)
		
			
EmailField = {
	"input":True,
	"hidden":False,
	"inputType":"email",
	"inputMask":"",
	"label":"",
	"helpText":"",
	"key":"",
	"placeholder":"",
	"suffix":"",
	"multiple":"",
	"defaultValue":"",
	"unique":"",
	"validation": {
		"required":"",
		"minLength":"",
		"maxLength":"",
		"pattern":"",
		"custom":"",
		"customPrivate":"",
	},
	"classes": [],
	"id":"",
	"customTemplate":""	
}

DateTimeField = {
	"input":True,
	"hidden":False,
	"inputType":"text",
	"inputMask":"",
	"enableDate":True,
	"enableTime":True,
	"format":"yyyy-MM-dd HH:mm",
	"label":"",
	"helpText":"",
	"key":"",
	"placeholder":"",
	"suffix":"",
	"multiple":"",
	"defaultValue":"",
	"unique":"",
	"validation": {
		"required":"",
		"minLength":"",
		"maxLength":"",
		"pattern":"",
		"custom":"",
		"customPrivate":"",
	},
	"classes": [],
	"id":"",
	"customTemplate":""	
}

"""

NEED TO USE THE DATETIMEPICKER SETTINGS

datepickerMode: "day",
-datePicker: {
showWeeks: true,
startingDay: 0,
initDate: "",
minMode: "day",
maxMode: "year",
yearRange: "20",
datepickerMode: "day"
},
-timePicker: {
hourStep: 1,
minuteStep: 1,
showMeridian: true,
readonlyInput: false,
mousewheel: true,
arrowkeys: true
},
		

- {
input: true,
inputType: "checkbox",
tableView: true,
hideLabel: true,
label: "",
key: "checkboxField",
defaultValue: false,
protected: false,
persistent: true,
-validate: {
required: false
},
type: "checkbox",
$$hashKey: "object:2015",
-conditional: {
show: false,
when: null,
eq: ""
}
},
- {
input: true,
tableView: true,
label: "",
key: "selectboxesField",
-values: [
- {
value: "test",
label: "test"
},
- {
value: "test1",
label: "test1"
}
],
-defaultValue: {
},
inline: false,
protected: false,
persistent: true,
-validate: {
required: false
},
type: "selectboxes",
$$hashKey: "object:2091",
-conditional: {
show: false,
when: null,
eq: ""
}
},
- {
input: true,
tableView: true,
label: "",
key: "selectField",
placeholder: "",
-data: {
-values: [
- {
value: "",
label: "",
$$hashKey: "object:2397"
}
],
json: "",
url: "",
resource: ""
},
dataSrc: "values",
valueProperty: "",
defaultValue: "",
refreshOn: "",
filter: "",
authenticate: false,
template: "{{ item.label }}",
multiple: false,
protected: false,
unique: false,
persistent: true,
-validate: {
required: false
},
type: "select",
$$hashKey: "object:2225",
-conditional: {
show: false,
when: null,
eq: ""
}
},
- {
input: true,
tableView: true,
label: "",
key: "textareaField",
placeholder: "",
prefix: "",
suffix: "",
rows: 3,
multiple: false,
defaultValue: "",
protected: false,
persistent: true,
wysiwyg: false,
-validate: {
required: false,
minLength: "",
maxLength: "",
pattern: "",
custom: ""
},
type: "textarea",
$$hashKey: "object:1887",
-conditional: {
show: false,
when: null,
eq: ""
}
},
- {
input: true,
tableView: true,
label: "",
key: "resourceField",
placeholder: "",
resource: "",
project: "",
defaultValue: "",
template: "{{ item.data }}",
selectFields: "",
searchFields: "",
multiple: false,
protected: false,
persistent: true,
-validate: {
required: false
},
defaultPermission: "",
type: "resource",
isNew: true,
$$hashKey: "object:3279"
},
- {
input: true,
tableView: true,
label: "",
key: "file",
placeholder: "",
multiple: false,
defaultValue: "",
protected: false,
type: "file",
$$hashKey: "object:3355",
-conditional: {
show: false,
when: null,
eq: ""
}
},
- {
input: true,
label: "Submit",
tableView: false,
key: "submit",
size: "md",
leftIcon: "",
rightIcon: "",
block: false,
action: "submit",
disableOnInvalid: true,
theme: "primary",
type: "button",
$$hashKey: "object:16"
}
],
display: "form",
page: 0
}
"""




TextField = ''
DateField = ''
DateTimeField = ''
IntegerField = ''
DecimalField = ''
ImageField = ''
FileField = ''
URLField = ''
EmailField = ''
