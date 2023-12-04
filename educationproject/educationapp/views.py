from django.http import HttpResponse
from django.shortcuts import render
# from . models import place
from . models import actor

# Create your views here.
# def demo(request):
#     obj= place.objects.all()
#     return render(request,"index.html",{'result':obj})
def demo(request):
    obj= actor.objects.all()
    return render(request,"index.html",{'result':obj})