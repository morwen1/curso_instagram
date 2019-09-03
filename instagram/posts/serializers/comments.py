from rest_framework import serializers
from posts.models import Comment
from users.serializers import ProfileSerializer
from rest_framework_recursive.fields import RecursiveField


"""class CommentSerializereply(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model=Comment
        fields ='__all__'
"""

class CommentSerializer(serializers.ModelSerializer):
    """
    este serializer es el serializer de los comentarios 
    tiene un modelo recursivo y utilizando la libreria de recursive de 
    rest_framework funciona perfecto
    """
    profile = ProfileSerializer(read_only=True)
    reply = RecursiveField(allow_null=True , many=True)
    class Meta:
        model=Comment
        fields =['id' , 'profile' , 'reply' ,'text']