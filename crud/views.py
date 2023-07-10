from django.shortcuts import redirect, render
from myapp.models import *
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html')


def dashboard(request):
    emp = Employee.objects.filter(user=-1).order_by('-id')
    if request.user.is_authenticated:
        emp = Employee.objects.filter(user=request.user).order_by('-id')
    page = Paginator(emp, 5)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    count = emp.count()


    context = {
        'count': count,
        'page':page,
    }
    return render(request, 'dashboard.html', context)

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employee(
            user = request.user,
            name=name, 
            email=email, 
            address=address, 
            phone=phone
        )
        emp.save()
        return redirect('dashboard')

    return render(request, 'dashboard.html')

def edit(request, id):
    emp = Employee.objects.get(id=id)
    context = {
        'emp': emp,
    }
    return render(request, 'dashboard.html', context)

def update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employee.objects.get(id=id)
        emp.name = name
        emp.email = email
        emp.address = address
        emp.phone = phone
        emp.save()

        return redirect('dashboard')

    return render(request, 'dashboard.html')

def delete(request, id):
    emp = Employee.objects.get(id=id)
    emp_name = emp.name
    emp.delete()
    context = {
        'emp_name': emp_name,
    }
    return redirect('dashboard')



def sign_up(request):   
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist!")
            return redirect('sign_up')
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('sign_up')
        
        if pass1 != pass2:
            messages.error(request, "Password didn't match!")
            return redirect('sign_up')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        subject = 'Employee Registration Confirmation'
        message = 'Thank you for registering in Employee!'
        from_email = 'dhruvilantala123@gmail.com'
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

        return render(request, 'signin.html', {'success': True})

    return render(request,'signup.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        
        user = authenticate(request,username=username,password=pass1)
        # print(user)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, 'signin.html')

def sign_out(request):
    logout(request)
    return redirect('home')


    




