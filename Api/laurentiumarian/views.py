from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *

class AppsView(APIView):
    def get(self, request, format=None):
        queryset = Apps.objects.all()
        serializer = CustomAppsSerializer(queryset, many=True)

        data = [{
                "NavApps": [],
                "LaunchPad": [],
                "Notifications": [],
                "Description": []
            }]

        for app in serializer.data:
            try:
                if app["img"] != None:
                    img = "https://api.laurentiumarian.ro" + app["img"]
                    app["img"] = img
                for i in range(len(data[0]["NavApps"])):
                    
                    if data[0]["NavApps"][i]["name"] == app["app"]["name"]:
                        data[0]["NavApps"][i]["apps"].append(app)
                        break
                else:
                    data[0]["NavApps"].append({
                        "name": app["app"]["name"],
                        "apps": [app]
                    })
            except:
                pass
        
        queryset = queryset.filter(type="App")
        serializer = AppsSerializer(queryset, many=True)

        for app in serializer.data:
            try:
                img = "https://api.laurentiumarian.ro" + app["img"]
            except:
                img = None
            app["img"] = img
            data[0]["LaunchPad"].append(app)

        queryset = Notifications.objects.all()
        serializer = NotificationsSerializer(queryset, many=True)

        for app in serializer.data:
            try:
                img = "https://api.laurentiumarian.ro" + app["img"]
            except:
                img = None
            app["img"] = img
            data[0]["Notifications"].append(app)

        queryset = Description.objects.all()
        serializer = DescriptionSerializer(queryset, many=True)
        for app in serializer.data:
            data[0]["Description"].append(app["data"])

        return Response(data,status=200)
