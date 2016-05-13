from __future__ import unicode_literals

import uuid
from django.db import models

# Create your models here.


stateChoices = (
('MA', 'Massachusetts'),
('RI', 'Rhode Island'),
('CT', 'Connecticut'),
('NH', 'New Hampshire'),
('ME', 'Maine'),
('AK', 'Alaska'),
('AL', 'Alabama'),
('AR', 'Arkansas'),
('AS', 'American Samoa'),
('AZ', 'Arizona'),
('CA', 'California'),
('CO', 'Colorado'),
('DC', 'District_of_Columbia'),
('DE', 'Delaware'),
('FL', 'Florida'),
('GA', 'Georgia'),
('GU', 'Guam'),
('HI', 'Hawaii'),
('IA', 'Iowa'),
('ID', 'Idaho'),
('IL', 'Illinois'),
('IN', 'Indiana'),
('KS', 'Kansas'),
('KY', 'Kentucky'),
('LA', 'Louisiana'),
('MD', 'Maryland'),
('MI', 'Michigan'),
('MN', 'Minnesota'),
('MO', 'Missouri'),
('MP', 'Northern_Mariana_Islands'),
('MS', 'Mississippi'),
('MT', 'Montana'),
('NA', 'National'),
('NC', 'North Carolina'),
('ND', 'North Dakota'),
('NE', 'Nebraska'),
('NJ', 'New Jersey'),
('NM', 'New Mexico'),
('NV', 'Nevada'),
('NY', 'New York'),
('OH', 'Ohio'),
('OK', 'Oklahoma'),
('OR', 'Oregon'),
('PA', 'Pennsylvania'),
('PR', 'Puerto Rico'),
('SC', 'South Carolina'),
('SD', 'South Dakota'),
('TN', 'Tennessee'),
('TX', 'Texas'),
('UT', 'Utah'),
('VA', 'Virginia'),
('VI', 'Virgin Islands'),
('VT', 'Vermont'),
('WA', 'Washington'),
('WI', 'Wisconsin'),
('WV', 'West Virginia'),
('WY', 'Wyoming'),)



class Address(models.Model):
	
	"""
	
	Base model for US-Based Addresses
	
	"""

	uuid = models.UUIDField(default=uuid.uuid4, editable=False)
	street1 = models.CharField(max_length=250)
	street2 = models.CharField(max_length=250, blank=True, null=True)
	city = models.CharField(max_length=250)
	state = models.CharField(max_length=250, choices=stateChoices)
	zipCode = models.CharField(max_length=15)
	lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
	long = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
	
	class Meta:
		abstract = True
		
	def state_choices(self):
		return stateChoices


class Telephone(models.Model):
	
	"""
	
	Base model for telephones, including utility functions
	
	"""
	
	uuid = models.UUIDField(default=uuid.uuid4, editable=False)
	telephone = models.CharField(max_length=200)
	
	class Meta:
		abstract = True

	def clean_phone(self):
		phone = self.telephone
		stripped = phone.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
		firstThree = stripped[:3]
		middleThree = stripped[3:6]
		lastFour = stripped[6:10]
		clean = '(' + firstThree + ') ' + middleThree + '-' + lastFour	   
		return clean
		
	def save(self, *args, **kwargs):
		clean = self.clean_phone()
		self.telephone = clean						
		super(Telephone, *args, **kwargs)
		
	
class Email(models.Model):
	
	"""
	
	Base model for emails, including utility functions
	
	"""
	
	uuid = models.UUIDField(default=uuid.uuid4, editable=False)
	email = models.EmailField()
	
	class Meta:
		abstract = True
