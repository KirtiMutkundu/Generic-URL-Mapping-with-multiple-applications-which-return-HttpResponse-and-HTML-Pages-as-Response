from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def msd(request):
    return render(request,'msd.html')
def ruturaj(request):
    return HttpResponse('RUTURAJ IS PLAYER OF CSK')