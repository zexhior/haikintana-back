from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import *
from .serilalizers import *

#CRUD
def read_all(serializer, model):
    items = model.objects.all()
    serial = serializer(items, many=True)
    return serial

def read(serializer, pk, model):
    serial = serializer(model.objects.get(id=pk))
    return serial

def create(serializer, request):
    serial = serializer(data=request.data)

    if serial.is_valid():
        serial.save

    return serial

def update(serializer, pk, model, request):
    item = model.objects.get(id=pk)
    serial = serializer(instance=item, data=request.data)

    if serial.is_valid():
        serial.save

    return serial

def delete(serializer, pk, model):
    item = model.objects.get(id=pk)
    item.delete()

@api_view(['GET'])
def home(requet):
    return Response(read_all(MembreSerializer, Membre).data)

@csrf_exempt
def membre_list(request):
    if request.method == "GET":
        return JsonResponse(read_all(MembreSerializer, Membre).data, safe=False)
    elif request.method == "POST":
        return JsonResponse(create(MembreSerializer, request).data, safe=False)

@csrf_exempt
def membre_get_update_delete(request, pk):
    try:
        membre = Membre.objects.get(id=pk)
        if request.method == "GET":
            return JsonResponse(read(MembreSerializer, pk, Membre).data)
        elif request.method == "PUT":
            return JsonResponse(update(MembreSerializer, pk, Membre, request))
        else:
            return HttpResponse(delete(MembreSerializer, pk, Membre))
    except Membre.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        customers_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Customer.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def customer_detail(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        customer_serializer = CustomerSerializer(customer)
        return JsonResponse(customer_serializer.data)

    elif request.method == 'PUT':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(customer, data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse(customer_serializer.data)
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)