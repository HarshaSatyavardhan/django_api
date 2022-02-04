from attr import field
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Researchpaper

class researchpaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Researchpaper
        fields = '__all__'
