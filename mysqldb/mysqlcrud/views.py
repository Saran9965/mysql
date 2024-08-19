from django.shortcuts import render
from .forms import myregisterForm

def home(req):
    return render(req,'home.html')

def insert(req):
    form=myregisterForm()
    return render(req,'register.html',{'form':form})
