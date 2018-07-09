from rest_framework.views import APIView
import json
from rest_framework.response import Response
from .models import Coin, AlertSerializer, Session, SessionSerializer

# Create your views here.
class Alert(APIView):
    def get(self, request, session_id):
        
        try:
            coin = Coin.objects.get(id=session_id)
        except Coin.DoesNotExist:
            return Response({ msg: "Coin not found"}, status=404)
            
        serializer = AlertSerializer(coin, many=True)

        return Response(serializer.data)    
        
    def post(self, request):
        return Response("EUREKA")
        
    def delete(self, request):
        return Response("Deleted")
        
class SessionView(APIView):        
    def post(self, request):
        
        body_unicode = request.body.decode('utf-8')
        c = json.loads(body_unicode)
        
        session=Session(email=c['email'], phone=c['phone'])
        session.save()
        
        serializer = SessionSerializer(session, many=False)
        
        return Response(serializer.data)
        # try:
        #     coin = Coin.objects.get(id=SessionID)
        
        #     body_unicode = request.body.decode('utf-8')
        #     c = json.loads(body_unicode)
            
        #     coin.coin_name=c['coin_name']
        #     coin.save()

        # except Coin.DoesNotExist:
        #     return Response({ msg: "Coin not found"}, status=404)
        # #serialize de contact
        # serializer = AlertSerializer(coin, many=False)
        # #include it on the response
        # return Response(serializer.data)
        
class CoinSearch(APIView):
    def get(self, request, coin_id):
        return Response("Coin Search!")
    
        #try:
      #      coin = Coin.objects.get(id=coinID)
      #  except Coin.DoesNotExist:
       #     return Reponse({ msg: "Coin not found"}, status=404)
            
      # serializer = AlertSerializer(coin, many=False)
        
      #  return Response(serializer.data)