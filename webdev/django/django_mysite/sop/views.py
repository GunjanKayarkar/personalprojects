from asyncio.windows_events import NULL
from django.http.response import JsonResponse

# Create your views here.
from rest_framework import status
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction 
# Create your views here.
@api_view(['GET'])
@transaction.atomic
@csrf_exempt
def loginhtml(request):
      
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "index.html")
@api_view(['GET'])
@transaction.atomic
@csrf_exempt

def registra(request):
    return render(request, "registration.html")

@api_view(['POST'])
@transaction.atomic
@csrf_exempt


def regdetail(request):
    print(request.data)
    reg = RegistrS(data=request.data)
    if reg.is_valid():
        reg.save()
        return JsonResponse(reg.data,status=status.HTTP_200_OK)
    return JsonResponse(reg.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@transaction.atomic
@csrf_exempt


def regdetailpa(request):
    
    cat_id = request.query_params.get('id', None)
    if(cat_id == NULL):
        data = Registr.objects.all()
    if(cat_id is not NULL):
        data = Registr.objects.filter(id=cat_id)
    R = RegistrS(data,many=True)
    return JsonResponse(R.data,safe=False,status=status.HTTP_200_OK)
