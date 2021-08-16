from django.shortcuts import render

# Create your views here.
from .models import test
def index(request):
	test1= test()
	test1.name= "al imran khan"
	test1.age= 23
	test1.pict= "U01.jpg"
	return render( request, 'test.html',{'test1': test1}, )
