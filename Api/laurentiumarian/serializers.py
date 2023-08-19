from rest_framework import serializers
from .models import NavApps, Apps

class NavAppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavApps
        fields = ['name']

class CustomAppsSerializer(serializers.ModelSerializer):
    app = NavAppsSerializer()  # Utilizați serializatorul NavAppsSerializer pentru câmpul 'app'

    class Meta:
        model = Apps
        fields = ['app', 'name', 'type', 'img' ]

class AppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apps
        fields = '__all__'