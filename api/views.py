from django.db.models import fields
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import request
from rest_framework import serializers
from .models import Researchpaper
from .serializer import researchpaperSerializer

@api_view(['GET'])
def getResearchpapers(request):
    researchpaper_all =  Researchpaper.objects.all()
    serializer = researchpaperSerializer(researchpaper_all, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getResearchpaper(request, pk):
    researchpaper_all =  Researchpaper.objects.get(id=pk)
    serializer = researchpaperSerializer(researchpaper_all, many=False)
    return Response(serializer.data)
