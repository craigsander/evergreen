from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from datetime import date, datetime, timedelta
from itertools import chain
from django.db.models import Q
from operator import attrgetter
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, get_object_or_404

from . import models

# Create your views here.

def page(request, slug, template_name='page.html'):

    page = get_object_or_404(models.Page, slug=slug, published=True)

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))
