from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from datetime import date, datetime, timedelta
from itertools import chain
from django.db.models import Q
from operator import attrgetter
from django.contrib.auth.decorators import login_required

def index(request, template_name='index.html'):
	
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))
