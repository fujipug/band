from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,"home.html",{})
def contacts(request):
    return render(request,"contacts.html",{})
def bio(request):
    return render(request,"bio.html",{})
def tourdates(request):
    return render(request,"tourdates.html",{})

