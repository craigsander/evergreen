
""" 

The goal here is to create a JSON-style validation model for common form inputs, similar to what Django does with it's models.Model.

At first we simply need to create a basic model with some basic attributes that can autopopulate JSONFields with the proper model. For now, this is to build the form element on the user end for dynamic forms.

We will later need to add some verification methods, again, similar to what Django does in Python.


http://codepen.io/travist/full/xVyMjo/

Checkout form.io. It's exactly what you're discussing. It's the same thing. 

Things I really like:
- Multiple - like SheepIt (http://stackoverflow.com/questions/34532871/add-multiple-fields-to-form)
- Plugins to handle drag-and-drop files, etc.


-components: [
- {
input: true,
tableView: true,
inputType: "text",
inputMask: "",
label: "",
key: "textField",
placeholder: "",
prefix: "",
suffix: "",
multiple: false,
defaultValue: "",
protected: false,
unique: false,
persistent: true,
-validate: {
required: false,
minLength: "",
maxLength: "",
pattern: "",
custom: "",
customPrivate: false
},
-conditional: {
show: false,
when: null,
eq: ""
},
type: "textfield",
$$hashKey: "object:1763"
},
- {
input: true,
tableView: true,
inputType: "text",
inputMask: "(617) 688-0988 (formatting)",
label: "Test",
key: "test",
placeholder: "Test",
prefix: "$",
suffix: "#",
multiple: true,
defaultValue: "Test",
protected: false,
unique: false,
persistent: true,
-validate: {
required: false,
minLength: "",
maxLength: "",
pattern: "",
custom: "",
customPrivate: false
},
-conditional: {
show: false,
when: null,
eq: ""
},
type: "textfield",
$$hashKey: "object:1249",
customClass: "large-12 columns"
},
- {
input: true,
tableView: true,
inputType: "email",
label: "Email",
key: "email",
placeholder: "",
prefix: "",
suffix: "",
defaultValue: "",
protected: false,
unique: false,
persistent: true,
type: "email",
$$hashKey: "object:2701",
-conditional: {
show: false,
when: null,
eq: ""
}
},
- {
input: true,
tableView: true,
inputMask: "(999) 999-9999",
label: "Phone",
key: "phone",
placeholder: "",
prefix: "",
suffix: "",
multiple: false,
protected: false,
unique: false,
persistent: true,
defaultValue: "",
-validate: {
required: false
},
type: "phoneNumber",
$$hashKey: "object:2836",
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
key: "addressField",
placeholder: "",
multiple: false,
protected: false,
unique: false,
persistent: true,
-validate: {
required: false
},
type: "address",
$$hashKey: "object:2972",
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
key: "datetimeField",
placeholder: "",
format: "yyyy-MM-dd HH:mm",
enableDate: true,
enableTime: true,
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
protected: false,
persistent: true,
-validate: {
required: false,
custom: ""
},
type: "datetime",
$$hashKey: "object:3105",
-conditional: {
show: false,
when: null,
eq: ""
}
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

CharField = {

}


TextField = ''
DateField = ''
DateTimeField = ''
IntegerField = ''
DecimalField = ''
ImageField = ''
FileField = ''
URLField = ''
EmailField = ''
