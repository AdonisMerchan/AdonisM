from django.shortcuts import render
from .models import taller1

# Create your views here.

def taller(request):
    select=taller1.objects.all()
    return render(request,'base.html',{"Envia":select})
