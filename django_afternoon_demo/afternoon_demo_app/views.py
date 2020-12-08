from django.shortcuts import render, HttpResponse, redirect
from django.template.defaulttags import register

# This helps us make a for loop with a number range since jinja + django is a pain
@register.filter
def get_range(value):
    return range(value)

# Create your views here.
def index(request):
    return render(request, "index.html")

def bio(request):
    return render(request, "bio.html")

def redir(request):
    return redirect("/")

def manyyodas(request, val):
    context = {
        'val': val,
        'range': range(val)
    }
    return render(request, "many.html", context)