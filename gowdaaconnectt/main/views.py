from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Business, Category, Contact


# ---------- MAIN PAGES ----------

def home(request):
    businesses = Business.objects.all()[:6]
    return render(request, 'home.html', {'businesses': businesses})


def about(request):
    return render(request, 'about.html')


def services(request):
    categories = Category.objects.all()
    return render(request, 'services.html', {'categories': categories})


def directory(request):

    q = request.GET.get('q')
    businesses = Business.objects.all()

    if q:
        businesses = businesses.filter(name__icontains=q)

    return render(request, 'directory.html', {'businesses': businesses})


def contact(request):

    if request.method == 'POST':

        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message']
        )

        messages.success(request, "Message sent!")

        return redirect('contact')

    return render(request, 'contact.html')


# ---------- AUTH SYSTEM ----------

def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registered! Please login.")

        return redirect('login')

    return render(request, 'register.html')


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is None:

            if not User.objects.filter(username=username).exists():

                messages.error(
                    request,
                    "Account not found! Please register first."
                )

                return redirect('register')

            else:
                messages.error(request, "Wrong password!")
                return redirect('login')

        login(request, user)

        return redirect('home')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def search(request):
    return render(request, 'search.html')
