from django.shortcuts import render,redirect
from .models import Bus,BusCompany,Prices
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            messages.info('Passwords not matching')
            return redirect(request.build_absolute_uri('/ugtransport/register'))
        if User.objects.filter(email=email).exists():
            messages.info('Email already exists')
            return redirect(request.build_absolute_uri('/ugtransport/register'))
        elif User.objects.filter(username=username).exists():
            messages.info('Username already taken')
            return redirect(request.build_absolute_uri('/ugtransport/register'))
        else:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
            user.save()
            return redirect(request.build_absolute_uri('/ugtransport/login'))

    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(request.build_absolute_uri('/ugtransport/district'))
        else:
            messages.info('Invalid Credentials')
            return redirect(request.build_absolute_uri('/ugtransport/login'))
    return render(request, 'login.html')

def home(request):
    companies = BusCompany.objects.all().order_by('region')
    return render(request,'home.html',{
        'companies' : companies
    })

def district(request,region):
    buses = Bus.objects.filter(mainOffices=region)
    return render(request,'region.html',{
        'buses':buses
    })

def company(request,company):
    companydetails = Bus.objects.filter(company=company)
    return render(request,'busCompany.html',{
        'buscompanies' : companydetails
    })

def busShift(request,id):
    shift = Bus.objects.get(id=id)
    return render(request,'busShift.html',{
       'shift': shift,
       'shift_id' : id,
       
    })

def bookShift(request):
    busId = request.POST.get('shift_id')
    shiftSeats = Bus.objects.get(id=busId) #shiftSeats is just an object
    shiftSeats.seats = int(shiftSeats.seats) - 1
    shiftSeats.save() #save the object
    return render(request, 'booked.html')