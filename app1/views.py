from django.shortcuts import render
from app1.forms import *
from django.http import HttpResponse
# Create your views here.
def djangoforms(request):
    so=Signup()
    d={'so':so}
    if request.method=='POST':
        sd=Signup(request.POST)
        if sd.is_valid():
            name=sd.cleaned_data['name']
            return HttpResponse(str(sd.cleaned_data))
       
    return render(request,'djangoforms.html',d)
