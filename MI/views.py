from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rohit(request):
    return render(request,'rohit.html')
def hardik(request):
    return HttpResponse('HARDIK IS PLAYER OF MI')