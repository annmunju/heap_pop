from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def commute(request):
    return render(request, 'commute.html')