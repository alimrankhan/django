from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.models import User, auth
def index(request):
    if request.method == 'POST' :
        fname= request.POST['fname']
        lname= request.POST['lname']
        username= request.POST['username']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']

        user= User.objects.create_user(first_name= fname, last_name= lname, username= username, email= email, password= password1)
        user.save();
        print('User registerd')
        return redirect('/')
# TODO: check password, username, email validation
    else:
        return render(request,'reg.html', {'method':request.method})
# TODO: create login logout
