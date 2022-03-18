from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from models import GearLevels

class GearLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GearLevels
        fields = '__all__'
