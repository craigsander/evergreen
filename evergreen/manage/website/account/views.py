from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from datetime import date, datetime, timedelta
from itertools import chain
from django.db.models import Q
from operator import attrgetter
from django.contrib.auth.decorators import login_required

import evergreen

#############################
# ACCOUNT
#############################

@login_required
def accounts(request, template_name='_accounts.html'):
	accounts = evergreen.website.account.models.UserProfile.objects.all()
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))
	
@login_required
def account(request, aid, template_name='_account.html'):
	account = get_object_or_404(evergreen.website.account.models.UserProfile, id=aid)
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))
