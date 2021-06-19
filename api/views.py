from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view,action
from rest_framework.parsers import JSONParser
from rest_framework import status,viewsets

from .forms import UploadFileForm

from .serilalizers import *

import cv2
from pyzbar.pyzbar import decode
import os
from pathlib import Path
from base64 import b64decode

BASE_DIR = Path(__file__).resolve().parent.parent
test= False;

class MembreCreation(viewsets.ModelViewSet):
    queryset = PhotoProfil.objects.all()
    serializer_class = PhotoProfilSerializer

    def post(self, request, *args, **kwargs):
        membre = int(request.data['membre'])
        photo = request.data['photo']
        try:
            photoprofil = PhotoProfil.objects.create(membre=membre, photo=photo)
            serial = PhotoProfilSerializer(data=photoprofil)
            if serial.is_valid():
                return JsonResponse(serial.data)
            else:
                return JsonResponse(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return JsonResponse("erreur",status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods='put')
    def put(self, request, pk=None):
        id = int(request.data['id'])
        photo = request.data['photo']

        try:
            photoprofil = PhotoProfil.objects.get(id=id)
            photoprofil.photo = photo
            photoprofil.save()
            return HttpResponse("Modification reussie", status=status.HTTP_200_OK)
        except PhotoProfil.DoesNotExist:
            return HttpResponse("erreur",status=status.HTTP_400_BAD_REQUEST)



class PhotoCreation(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def post(self, request, *args, **kwargs):
        image = request.data['url_image']
        activite = int(request.data['activite'])

        try:
            photo = Photo.objects.create(url_image=image, activite=activite)
            serial = PhotoSerializer(data=photo)
            if serial.is_valid():
                return JsonResponse(serial.data)
            else:
                return JsonResponse(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return JsonResponse("erreur", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@csrf_exempt
def testCodeQr(request):
    image_data = JSONParser().parse(request);

    header, encoded = image_data['image'].split(",", 1)
    data = b64decode(encoded)

    with open(os.path.join(BASE_DIR, 'media/images/qr3.png'),"wb") as f:
        f.write(data)

    img = cv2.imread(os.path.join(BASE_DIR, 'media/images/qr3.png'))

    myData = ""
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
    if myData != "" :
        elements = myData.split('*')
        membre = Membre.objects.get(id=elements[0], nom=elements[1], prenom=elements[2])
        serial = MembreSerializer(membre)
        return JsonResponse(serial.data, safe=False)

    return JsonResponse(myData, safe=False)

#CRUD
def read_all(serializer, model):
    items = model.objects.all()
    serial = serializer(items, many=True)
    return serial

def read(serializer, pk, model):
    serial = serializer(model.objects.get(id=pk))
    return serial

def create(serializer, request):
    element = JSONParser().parse(request)
    serial = serializer(data=element)

    if serial.is_valid():
        serial.save()
        return JsonResponse(serial.data)

    return JsonResponse(serial.errors, status=status.HTTP_400_BAD_REQUEST)

def update(serializer, pk, model, request):
    item = model.objects.get(id=pk)
    element = JSONParser().parse(request)
    serial = serializer(item, data=element)

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
        return create(serializer, request)
    else:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

@action(detail=True, methods='put')
def object_get_update_delete(serializer, model, request, pk):
    try:
        if request.method == "GET":
            return JsonResponse(read(serializer, pk, model).data)
        elif request.method == "PUT":
            return JsonResponse(update(serializer, pk, model, request).data)
        else:
            return HttpResponse(delete(serializer, pk, model))
    except Membre.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def home(request):
    return Response(read_all(MembreSerializer, Membre).data)

@csrf_exempt
def membre_list(request):
    return object_list(MembreSaveSerializer, Membre, request)


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
    return object_list(ActiviteSaveSerializer, Activite, request)

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

@csrf_exempt
def contact_organisation_list(request):
    return object_list(ContactOrganisationSerializer, ContactOrganisation, request)

@csrf_exempt
def contact_organisation_get_update_delete(request, pk):
    return object_get_update_delete(ContactOrganisationSerializer, ContactOrganisation, request, pk)

@csrf_exempt
def regle_list(request):
    return object_list(RegleSerializer, Regle, request)

@csrf_exempt
def regle_get_update_delete(request, pk):
    return object_get_update_delete(RegleSerializer, Regle, request, pk)

@csrf_exempt
def cotisation_list(request):
    return object_list(CotisationSerializer, Cotisation, request)

@csrf_exempt
def cotisation_get_update_delete(request, pk):
    return object_get_update_delete(CotisationSerializer, Cotisation, request, pk)

@csrf_exempt
def paiement_list(request):
    return object_list(PaiementSerializer, Paiement, request)

@csrf_exempt
def paiement_get_update_delete(request, pk):
    return object_get_update_delete(PaiementSerializer, Paiement, request, pk)

@csrf_exempt
def photoprofil_list(request):
    return object_list(PhotoProfilSerializer, PhotoProfil, request)

@csrf_exempt
def photoprofil_get_update_delete(request, pk):
    return object_get_update_delete(PhotoProfilSerializer, PhotoProfil, request, pk)

@api_view(['PUT'])
def update_membre(request,pk):
    return Response(update(MembreSerializer,pk,Membre,request).data)
