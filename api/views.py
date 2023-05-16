from rest_framework.views import APIView
from rest_framework.response import Response
from .response import answer

class Answer(APIView):
    
    def post(self,request):
        q = request.data['q']
        data = answer(q)
        data = {
            'a':data
        }
        return Response(data)
        
    