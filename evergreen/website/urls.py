from django.conf.urls import url, include
from django.conf import settings

from otto.website import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	url(r'^$', views.index),
	url(r'^{0}/'.format(settings.PAGE_ROOT_URL), include('otto.website.page.urls')),
]
