from rest_framework import serializers
from .models import NavApps, Apps

class NavAppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavApps
        fields = ['name']

class CustomAppsSerializer(serializers.ModelSerializer):
    app = NavAppsSerializer()


    class Meta:
        model = Apps
        fields = ['app', 'name', 'type', 'img', 'content' ]

class AppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apps
        fields = ['name', 'type', 'img', 'content']