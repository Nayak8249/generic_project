from django.shortcuts import render

from django.http import HttpResponse

def msd(request):
    return HttpResponse('msd is a cool caption in the world ')

def raina(request):
    return render(request,'raina.html')