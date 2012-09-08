from django.shortcuts import render_to_response
from django.template import RequestContext
from enlaces.models import Enlace

def inicio(request):
	enlaces = Enlace.objects.all().order_by('-fecha')
	return render_to_response('index.html', {'enlaces': enlaces}, context_instance=RequestContext(request))
