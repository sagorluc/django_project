from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from make_token_user_app.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from . import singnals

# Create your views here.
class RegistrationView(APIView):
    def post(self, request):
        serial = RegistrationSerializer(data= request.data)
        data = {} 
        if serial.is_valid():
            account = serial.save()
            data['response'] = 'Registration Successfull !!'
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user = account).key # generate token
            data['token'] = token
            Response(serial.data, status= status.HTTP_201_CREATED)
        else:
            data = serial.errors
        return Response(data)
    
class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status= status.HTTP_200_OK)
    
