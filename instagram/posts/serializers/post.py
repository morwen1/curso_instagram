from rest_framework import serializers
from posts.models import Post
from users.serializers import ProfileSerializer
from posts.serializers.comments import CommentSerializer

class PostSerializerfirst(serializers.ModelSerializer):
    profile= ProfileSerializer(read_only = True)
    
    class Meta:
        model = Post
        fields = (
            'profile',
            'photo',
            'likes',
            'description'
            
        )


class PostSerializer(serializers.ModelSerializer):
    profile= ProfileSerializer(read_only = True)
    comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = (
            'id',
            'profile',
            'photo',
            'likes',
            'description',
            'comments'
        )