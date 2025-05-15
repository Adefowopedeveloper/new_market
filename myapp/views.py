from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')
def home(request):
    return render(request, 'home.html')
def buy(request):
    return render(request, 'buy.html')
def rent(request):
    return render(request, 'rent.html')
def buy_house(request):
    return render(request, 'buy_house.html')
def buy_car(request):
    return render(request, 'buy_car.html')
def profile(request):
    return render(request, 'profile.html')

