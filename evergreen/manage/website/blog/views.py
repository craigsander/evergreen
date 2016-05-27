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

