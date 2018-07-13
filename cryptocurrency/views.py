from rest_framework.views import APIView
import json
from rest_framework.response import Response
from .models import Coin, AlertSerializer, Session, SessionSerializer, Notification, NotificationSerializer

# Create your views here.
class NotificationView(APIView):
    def get(self, request):
        """
        Return the list of notifications
        """
        data = request.GET
        print(data)
        # if "email" in data:
        #     email = data.get("email", None)
        # else: 
        #     email = None
        email = data.get("email", None)
        phone = data.get("phone", None)
        # 1 validate that the date existe (if the user sent and email and/or a phone number)
        # 1.1 if there is no email, and there is no phone, return an error
        if email is None and phone is None:
            return Response("I can't make a search without email or phone number", status=400)
        # 2 Filter the sessions for the data that the user send me (if necesary)
        # 2.1 if i have an email Filter all the sessions by that email
        
        # 2.2 If i have a phone filter all the session by that phone
        # 2.3 If i have an email and a phone filter the sessions by that email and that phone
        
        if email is not None:
            sessions_list = Session.objects.filter(email=email)
        if phone is not None:
            sessions_list = Session.objects.filter(phone=phone)
        if phone is not None and email is not None:
            sessions_list = Session.objects.filter(email=email, phone=phone)
        
        if len(sessions_list) < 1: # This means that the list is empty
            return Response("Session not found", status=400)
        
        session = sessions_list[0] # We only need one
        # Once i have the session, retrieve all the Notifications for that Session    
        notification_list = Notification.objects.filter(session=session)
        # we transform the django model into json types      
        serializer = NotificationSerializer(notification_list, many=True)
        #include it on the response
        return Response(serializer.data)

        
    def post(self, request):
        
        # 1) Receive the information
        body = request.body
        body_unicode = body.decode('utf-8')
        data = json.loads(body_unicode)
        print("THIS IS THE DATA: " + str(data))
        # 2) validate that the information is consistent
        email = data.get("email")
        phone = data.get("phone")
        price_delta = data.get("price_delta")
        volume_delta = data.get("volume_delta")
        coin = data.get("coin")
        # 3) Save that information to the databse using a Django Model (in this case)
        # 3.1) Search for a session with the email or phone
        sessions_list = Session.objects.filter(email=email, phone=phone)
        # 3.2) If a coin with that name does not exist, then create one
        if len(sessions_list) > 0: # This means that, at least one Coin exists with those conditions
           session = sessions_list[0]
        else: # This means that nothing of the database exists with this conditions
            session = Session() # Create a new Coin
            session.email = email
            session.phone = phone
            session.save()

        # 3.3) Search for a coin with the name
        coin_list = Coin.objects.filter(coin_name=coin)
        # 3.4) If a coin with that name does not exist, then create one
        if len(coin_list) > 0: # This means that, at least one Coin exists with those conditions
            new_coin = coin_list[0]
        else: # This means that nothing of the database exists with this conditions
            new_coin = Coin() # Create a new Coin
            new_coin.coin_name = coin
            new_coin.save()
            
        # 3.5) Create the notification
        notification = Notification() # Create a new notification
        notification.coin = new_coin
        notification.session = session
        notification.volume_delta = volume_delta
        notification.price_delta = price_delta
        notification.save()
        # 4) Maybe i want to return the information that was saved
        serializer = NotificationSerializer(notification, many=False)
        return Response(serializer.data)
        
    def delete(self, request):
        data = request.GET
        print(data)
      
        email = data.get("email")
        phone = data.get("phone")
        
        if email is None and phone is None:
            return Response("I can't delete that which does not exist", status=400)
       
        if email is not None:
            sessions_list = Session.objects.filter(email=email)
        if phone is not None:
            sessions_list = Session.objects.filter(phone=phone)
        if phone is not None and email is not None:
            sessions_list = Session.objects.filter(email=email, phone=phone)
        
        if len(sessions_list) < 1: # This means that the list is empty
            return Response("Session not found", status=400)
        
        session = sessions_list[0]
        session.delete()
       
        serializer = NotificationSerializer(sessions_list, many=False)
        return Response(serializer.data)
      
    
# class SessionView(APIView):        
#     def post(self, request):
        
#         body_unicode = request.body.decode('utf-8')
#         c = json.loads(body_unicode)
        
#         session=Session(email=c['email'], phone=c['phone'])
#         session.save()
        
#         serializer = SessionSerializer(session, many=False)
        
#         return Response(serializer.data)
#         # try:
#         #     coin = Coin.objects.get(id=SessionID)
        
#         #     body_unicode = request.body.decode('utf-8')
#         #     c = json.loads(body_unicode)
            
#         #     coin.coin_name=c['coin_name']
#         #     coin.save()

#         # except Coin.DoesNotExist:
#         #     return Response({ msg: "Coin not found"}, status=404)
#         # #serialize de contact
#         # serializer = AlertSerializer(coin, many=False)
#         # #include it on the response
#         # return Response(serializer.data)
        