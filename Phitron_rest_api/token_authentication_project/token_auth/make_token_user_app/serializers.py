from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    repassword = serializers.CharField(style= {"input_type": "password"}, write_only = 'True')
    class Meta:  
        model = User
        fields = ['username', 'email', 'password', 'repassword']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    # Get data
    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        repassword = self.validated_data['repassword']
        
        if password != repassword:
            raise serializers.ValidationError({'error': 'password does not matched'})
        
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'error': 'Email already exists'})
        
        account = User(username = username, email = email)
        account.set_password(password)
        account.save()
        return account