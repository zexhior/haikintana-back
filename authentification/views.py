from django.shortcuts import render
from ..api.models import *

def home(request):
    membre = Membre
    return render(request)
