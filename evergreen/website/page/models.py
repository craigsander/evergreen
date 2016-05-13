from __future__ import unicode_literals

# Python Libs
import uuid
from datetime import datetime, date, timedelta

# Django Built-Ins
from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import JSONField

newfields={'fields': {
	{'field1': {
		'required':True,
		'type': 'textarea',
		'html':True,
		'label':'',
		'help_text':'',		
		'classes':[],
		'content':'',
		},
	},
	{'field2': {
		'required':False,
		'type': 'select/multi',
		'options': {
			'value1':'option1',
			'value2':'option2',
			'value3':'option3',
		},
		'classes' = [],
		'label':'',
		'help_text': '',
		},	
	},
}

class PageType(models.Model):
	
	"""
	The page type supplies each page with a set of additional fields required for each page. For example, if the page type is 'Basic Page', then the fields might incorporate just a 'body' textfield.
	"""
	
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=250)
	template = models.CharField(max_length=200, help_text='Put the name of the template here, including the .html suffix.')
	fields = JSONField(blank=True,null=True)
	
	def __unicode__(self):
		return self.name


class Page(models.Model):
	
	"""
	This is the basic Page object. This object is a standalone item with a core set of fields.
	"""
	
	# universal fields
	pageType = models.ForeignKey('PageType')
	author = models.ForeignKey('account.UserProfile')
	authorDisplayValue = models.CharField(max_length=200, blank=True, null=True, help_text='If you want to display a name other than the person listed in the author field, enter the text here.')
	title = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	published = models.BooleanField(default=False)
	publishOn = models.DateField(null=True, blank=True, help_text='Set a date here to delay publishing of this page until a certain date. Publishing/Unpublishing takes effect around midnight of the date set.')
	expiresOn = models.DateField(null=True, blank=True, help_text='Set a date here to unpublish this page on a certain date. Publishing/Unpublishing takes effect around midnight of the date set.')

	# seo
	description = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250)
	
	def get_absolute_url(self):
		return '/{0}/{1}/'.format(settings.PAGE_ROOT_URL, self.slug)
	
	
	def __unicode__(self):
		return self.title

	def as_json(self):
		return None
		
	## TO DO
	'''
	On save, you need to validate the page type's json
	You need to check if there's already data in the fields
	If there's data in the POST, update
	If there's no data in the POST and no data in the data, but the field is required, send error back
	'''	
		
		
	# project-specific
#	title = models.CharField(blank=True, null=True)
#	body = models.TextField(blank=True, null=True)
#	callToActionTitle = models.CharField(blank=True, null=True)
#	callToActionBody = models.CharField(blank=True, null=True)
#	callToActionLink = models.CharField(blank=True, null=True)
#	callToActionButtonText = models.CharField=True, null=True)
