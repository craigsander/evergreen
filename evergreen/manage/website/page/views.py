from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from datetime import date, datetime, timedelta
from itertools import chain
from django.db.models import Q
from operator import attrgetter
from django.contrib.auth.decorators import login_required

import evergreen
ext(request))

#############################
# PAGE
#############################

@login_required
def pages(request, template_name='_pages.html'):
	pages = evergreen.website.page.models.Page.objects.all()
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))
	

@login_required
def page(request, pid, template_name='_page.html'):
	page = get_object_or_404(evergreen.website.page.models.Page, id=pid)
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))
	
