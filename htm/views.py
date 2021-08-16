from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse
from .models import Det

def index(request):
	
    return render(request,'hello.html',{'name':'Imran','age':22},)
