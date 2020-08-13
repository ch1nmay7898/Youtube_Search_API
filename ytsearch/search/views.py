from django.shortcuts import render
from django.conf import settings
from .models import SavedVids 
from .serializers import SavedVidsSerializer
from rest_framework import viewsets
from .tasks import API_call
import requests
import json

# API Consume function background.
def index(request):
    vids = SavedVids.objects.all()
    return API_call(repeat=40)

class SavedVidsViewSet(viewsets.ModelViewSet):
    queryset = SavedVids.objects.all().order_by('publishedAt')
    serializer_class = SavedVidsSerializer

# HTML Render page.
def view(request):
    
    vids = SavedVids.objects.all()
    return render(request, "search/index.html", {
        "vids": vids
    })