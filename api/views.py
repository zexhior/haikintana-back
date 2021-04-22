from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .forms import UploadFileForm

from .serilalizers import *

def handle_uploaded_file(file):
    photo = Photo()

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

def object_list(serializer, model, request):
    if request.method == "GET":
        return JsonResponse(read_all(serializer, model).data, safe=False)
    elif request.method == "POST":
        return JsonResponse(create(serializer, request).data, safe=False)
    else:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

def object_get_update_delete(serializer, model, request, pk):
    try:
        if request.method == "GET":
            return JsonResponse(read(serializer, pk, model).data)
        elif request.method == "PUT":
            return JsonResponse(update(serializer, pk, model, request))
        else:
            return HttpResponse(delete(serializer, pk, model))
    except Membre.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def home(requet):
    return Response(read_all(MembreSerializer, Membre).data)

@csrf_exempt
def membre_list(request):
    return object_list(MembreSerializer, Membre, request)


@csrf_exempt
def membre_get_update_delete(request, pk):
    return object_get_update_delete(MembreSerializer, Membre, request, pk)

@csrf_exempt
def numero_list(request):
    return object_list(NumeroSerializer, ContactNum, request)


@csrf_exempt
def numero_get_update_delete(request, pk):
    return object_get_update_delete(NumeroSerializer, ContactNum, request, pk)

@csrf_exempt
def fb_list(request):
    return object_list(FbSerializer, ContactFb, request)


@csrf_exempt
def fb_get_update_delete(request, pk):
    return object_get_update_delete(FbSerializer, ContactFb, request, pk)

@csrf_exempt
def mail_list(request):
    return object_list(MailSerializer, ContactMail, request)


@csrf_exempt
def mail_get_update_delete(request, pk):
    return object_get_update_delete(MailSerializer, ContactMail, request, pk)

@csrf_exempt
def categorie_list(request):
    return object_list(CategorieSerializer, Categorie, request)


@csrf_exempt
def categorie_get_update_delete(request, pk):
    return object_get_update_delete(CategorieSerializer, Categorie, request, pk)

@csrf_exempt
def activite_list(request):
    return object_list(ActiviteSerializer, Activite, request)

@csrf_exempt
def activite_get_update_delete(request, pk):
    return object_get_update_delete(ActiviteSerializer, Activite, request, pk)

@csrf_exempt
def description_list(request):
    return object_list(DescriptionSerializer, Description, request)


@csrf_exempt
def description_get_update_delete(request, pk):
    return object_get_update_delete(DescriptionSerializer, Description, request, pk)

@csrf_exempt
def photo_list(request):
    return object_list(PhotoSerializer, Photo, request)

@csrf_exempt
def photo_get_update_delete(request, pk):
    return object_get_update_delete(PhotoSerializer, Photo, request, pk)

@csrf_exempt
def presence_list(request):
    return object_list(PresenceSerializer, Presence, request)

@csrf_exempt
def presence_get_update_delete(request, pk):
    return object_get_update_delete(PresenceSerializer, Presence, request, pk)

@api_view(['PUT'])
def update_membre(request,pk):
    return Response(update(MembreSerializer,pk,Membre,request).data)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponse()