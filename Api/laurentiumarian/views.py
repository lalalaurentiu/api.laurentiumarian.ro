from rest_framework.response import Response
from rest_framework.views import APIView

class AppsView(APIView):
    def get(self, request):
        return Response({
            'laurentiumarian': 'hello world'})
