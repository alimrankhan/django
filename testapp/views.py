from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
	return render(request,'testapp.html',{'name':'Al Imran Khan'})

def add(request):
	return render(request,'add_num.html')

def add_dis(request):
	val1 = request.POST['num1']
	val2 = request.POST['num2']
	res= int(val1)+int(val2)
	return render(request,'add_res.html',{'result':res})

