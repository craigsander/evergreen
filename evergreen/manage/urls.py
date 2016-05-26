from django.conf.urls import url, include
from django.conf import settings

from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	url(r'manage/', views.index),
]
