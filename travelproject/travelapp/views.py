from django.shortcuts import render
from . models import place


def fun(request):
   obj=place.objects.all()
   return render(request,'index.html',{'results':obj})



