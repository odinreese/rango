# I import the HttpResponse object from the django.http module. 
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response


# Each view exists within the views.py file as a series of individual 
# functions. In this instance, we only created one view - called index
def index(request):
    context = RequestContext(request)
    context_dict ={'boldmessage': "I am bold font from the context"}
    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "This is the about page"}
    return render_to_response('rango/about.html', context_dict, context)
    

