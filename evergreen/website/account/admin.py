from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.UserProfileBaseSettings)
admin.site.register(models.UserProfile)
