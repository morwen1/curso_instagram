from rest_framework import serializers
from rest_framework import validators
from django.contrib.auth import password_validation, authenticate
from users.models import User,Profile



class register_Serializer (serializers.Serializer):

    email =serializers.EmailField(
        validators=[validators.UniqueValidator(queryset = User.objects.all())]
    )

    username=serializers.CharField(

        min_length = 2 , 
        max_length=100,
        validators = [validators.UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        min_length= 8 ,
        max_length=255
    )

    password_confirmation = serializers.CharField(
        min_length= 8 ,
        max_length=255
    )

    first_name = serializers.CharField(
        min_length= 2 ,
        max_length=100
    )

    last_name=serializers.CharField(
        min_length= 2 ,
        max_length=100
    )
    def validate(self , data):
        passwd = data['password']
        paswwd_conf = data['password_confirmation']
        if passwd != paswwd_conf:
            raise serializers.ValidationError('keys does not equals')
        
        password_validation.validate_password(passwd)
        return data

    def create(self , data):
        data.pop('password_confirmation')
        user=User.objects.create_user(**data , is_active=True)
        Profile.objects.create(user=user)
        return user
    
        
