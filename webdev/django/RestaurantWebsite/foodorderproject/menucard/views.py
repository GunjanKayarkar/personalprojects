from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(requests):
    return render(requests, 'menucard/main.html')

def main(requests):
    return render(requests, 'menucard/main.html')

def about(requests):
    return render(requests, 'menucard/about.html')

def index(requests):
    return render(requests, 'menucard/index.html')

def order(request):
	st=Menu.objects.all()
	return render(request,'menucard/order.html',{'st':st})

def order_form(requests):
    form = OrderForm()
    if requests.method == 'POST':
        print("request.post", requests.POST)

        form = OrderForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('menucard:order')
    context = {'form': form}
    return render(requests, 'menucard/order_form.html', context)

def showmain(request):
    last_order=Orderid.objects.last()
    return render(request,'menucard/showmain.html', {'last_order':last_order})

def showmain2(request):
	allorders=Orderid.objects.filter(order_status='Progressing')
	return render(request,'menucard/showmain2.html',{'allorders':allorders})

def showmain3(request):
	allorders=Orderid.objects.filter(order_status='completed')
	return render(request,'menucard/showmain3.html',{'allorders':allorders})

def showmain4(request):
	allorders=Orderid.objects.filter(order_status='prepared')
	return render(request,'menucard/showmain4.html',{'allorders':allorders})

@login_required(login_url='menucard:login')
def createform(requests):
    form = CreateForm()
    if requests.method == 'POST':
        print("request.post", requests.POST)

        form = CreateForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('menucard:order')
    context = {'form': form}
    return render(requests, 'menucard/createform.html', context)

@login_required(login_url='menucard:login')
def updateform(requests, id):
    obj = Menu.objects.get(id=id)
    form = UpdateForm(instance=obj)
    if requests.method == 'POST':
        form = UpdateForm(requests.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('menucard:order')
    context = {'form': form}
    return render(requests, 'menucard/updateform.html', context)

@login_required(login_url='menucard:login')
def deleteform(requests, id):
    obj = Menu.objects.get(id=id)
    if requests.method == 'POST':
        obj.delete()
        return redirect('menucard:order')
    context = {'item': obj}
    return render(requests, 'menucard/deleteform.html', context)

def signup(requests):
    if requests.method == 'POST':
        form = SignUpForm(requests.POST)

        if form.is_valid():
            user = form.save()
            login(requests, user)
            return redirect('menucard:home')
    else:
        form = SignUpForm()
    return render(requests, 'menucard/registration/signup.html', {'form': form})

def login(requests):
    return render(requests, 'menucard/registration/login.html')