from django.conf.urls import url, include
from django.conf import settings

from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	url(r'manage/', views.index),
	url(r'manage/website/', include('evergreen.manage.website.urls')),
	url(r'manage/account/', include('evergreen.manage.website.account.urls')),
	url(r'manage/page/', include('evergreen.manage.website.page.urls')),
	url(r'manage/blog/', include('evergreen.manage.website.blog.urls')),
	url(r'manage/content/', include('evergreen.manage.website.content.urls')),
]
