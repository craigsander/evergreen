from django.conf.urls import url, include
from django.conf import settings

from evergreen.website import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	url(r'^$', views.index),
	url(r'^{0}/'.format(settings.PAGE_ROOT_URL), include('evergreen.website.page.urls')),
	url(r'^{0}/'.format(settings.BLOG_ROOT_URL), include('evergreen.website.blog.urls')),
]
