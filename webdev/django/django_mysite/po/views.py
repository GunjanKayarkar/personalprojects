from django.shortcuts import render
from .models import *
from ..sop.serializers import *

# Create your views here.
def loginhtml(request):
      
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "index.html")

def registra(request):
    return render(request, "registration.html")

def regdetail(request):
    print(request.data)
    reg = Registration(data=request.data, many=True)
    if reg.is_valid():
        reg.save()
