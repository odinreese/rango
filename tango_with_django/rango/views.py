# I import the HttpResponse object from the django.http module. 
from django.http import HttpResponse


# Each view exists within the views.py file as a series of individual 
# functions. In this instance, we only created one view - called index
def index(request):
    # Each view takes in at least one argument - a HttpRequest object, which
    # also live in the django.http module. Convention dictates that this is
    # named request, but you can rename it to whatever you want.

    # Each view must return a HttpResponse object. A simple HttpResponse 
    # object takes a string parameter representing the content of the page
    # we wish to send to the client requesting the view.
    return HttpResponse("Rango says hello world! <a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("Rango says this is the about page. <a href='/rango/'>Main Page</a")


