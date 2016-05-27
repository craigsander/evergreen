from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from datetime import date, datetime, timedelta
from itertools import chain
from django.db.models import Q
from operator import attrgetter
from django.contrib.auth.decorators import login_required

import evergreen

@login_required
def index(request, template_name='_index.html'):	
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))


#############################
# WEBSITE
#############################



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
	
#############################
# BLOG
#############################

@login_required
def articles(request, template_name='_articles.html'):
	articles = evergreen.website.blog.models.Article.objects.all()
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))
	
@login_required
def article(request, aid, template_name='_article.html'):
	article = get_object_or_404(evergreen.website.blog.models.Article, id=aid)
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))


#############################
# FORM
#############################

@login_required
def forms(request, template_name='_forms.html'):
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))
	
@login_required
def form(request, template_name='_form.html'):
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))
	


## To Do: Create endpoint to CRUD Category
## TO DO: Create endpoint to CRUD Keyword
