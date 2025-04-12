from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def page_view(request):
    return HttpResponse("hlo world!!!!")
