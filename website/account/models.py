from __future__ import unicode_literals

# Python Libs
import uuid
from datetime import datetime, date, timedelta

# Django Built-Ins
from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ValidationError

# Add-ons and Custom Libs
from evergreen.utils import contact_information as ci


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)


class UserProfileBaseSettings(models.Model):
	data = JSONField(blank=True, null=True)
	
	def __unicode__(self):
		return 'User Profile Core Fields'

	def clean(self):
		validate_only_one_instance(self)


class UserProfile(models.Model):
	
	"""
	This is the base connection to the User object. This stores basic information about each user, beyond that requested, and in some cases, the same as, the User object.
	"""
	
	uuid = models.UUIDField(default=uuid.uuid4, editable=False)
	user = models.ForeignKey('auth.User')
	fName = models.CharField(max_length=200,blank=True, null=True)
	lName = models.CharField(max_length=200,blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	fromBase = JSONField(blank=True, null=True)
	data = JSONField(blank=True, null=True) # this is a test. I want a flexible way of handling storage of extra data; will this work?
	is_admin = models.BooleanField(default=False) # is_admin can create objects, manage objects, and really do anything except edit core owner-reserved information.
	is_active = models.BooleanField(default=True) # is_active means that the user can operate as a base user in the system		

	def __unicode__(self):
		return '{0} {1}'.format(self.fName, self.lName)
		
		
	## TO DO: If this is a new instance, get the additional data fields needed by the UserProfileBaseSettings
	## TO DO: Make sure that new user creation creates a corresponding UserProfile; Django Signals appears to be the answer.	

#	def save(self, *args, **kwargs):
#		if self.adding:
#			
#		super(ModelWithOnlyOneInstance, self).save(*args, **kwargs)
