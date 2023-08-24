from rest_framework import serializers
from .models import *

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

class DescriptionSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField('get_data')
    
    class Meta:
        model = Description
        fields = ['description', 'data']

    def get_data(self, obj):
        return {
            'name': obj.app.name,
            'type': obj.app.type,
            'img': "https://api.laurentiumarian.ro" + obj.app.img.url,
            'content': obj.app.content,
            'description': obj.description,
            'code': obj.code
        }

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ['name', 'img', 'content']

    