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
                "NavApps": []
            }
        ]

        for app in serializer.data:

            for i in range(len(data[0]["NavApps"])):
                if data[0]["NavApps"][i]["name"] == app["app"]["name"]:
                    data[0]["NavApps"][i]["apps"].append(app)
                    break
            else:
                data[0]["NavApps"].append({
                    "name": app["app"]["name"],
                    "apps": [app]
                })

        return Response(
            data,
            status=200

        )
