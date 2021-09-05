from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.models import User, auth
from django.contrib import messages
def index(request):
    if request.method == 'POST' :
        fname= request.POST['fname']
        lname= request.POST['lname']
        username= request.POST['username']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']
        if password1!=password2:
            print('password not matched')
            messages.info(request, "Password not matched")
            return redirect('/reg')
        elif(User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            print('username or email is already registerd')
            messages.info(request, "username or email is already registerd")
            return redirect('/reg')
        else:
            user= User.objects.create_user(first_name= fname, last_name= lname, username= username, email= email, password= password1)
            user.save();
            print('User registerd')
            messages.info(request, "User registerd successfully")
        return redirect('/reg')

    else:
        return render(request,'reg.html', )

def login(request):
    if request.method== 'POST':
        username= request.POST['username']
        password= request.POST['password']
        user= auth.authenticate(username= username, password= password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('/reg/login/')
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
