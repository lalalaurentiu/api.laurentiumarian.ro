from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *

class AppsView(APIView):
    def get(self, request):
        queryset = Apps.objects.all()
        serializer = CustomAppsSerializer(queryset, many=True)

        data = [
            {
                "NavApps": [],
                "LaunchPad": []
            }
        ]

        for app in serializer.data:
            try:
                img = "http://192.168.0.156:8000" + app["img"]
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
            img = "http://192.168.0.156:8000" + app["img"]
            app["img"] = img
            data[0]["LaunchPad"].append(app)


        return Response(
            data,
            status=200

        )
