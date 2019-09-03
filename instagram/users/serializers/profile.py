from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField


from users.models import Profile
from users.serializers import UserSerializer


class ProfileSerializer2dolevel(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model= Profile
        exclude = ('followers' , 'following')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    followers =ProfileSerializer2dolevel(read_only=True ,many=True, allow_null=True)
    following =ProfileSerializer2dolevel(read_only=True ,many=True,  allow_null=True)
    class Meta:
        model= Profile
        fields='__all__'
    

class FollowerSerializer(serializers.Serializer):
    profile_requester = ProfileSerializer(read_only=True)
    follower = serializers.IntegerField()
    
        
"""
    def delete(self, data):
        follower = Profile.objects.get(data['follower'])
        profile = Profile.objects.get(data['profile_requester'])
        follower.follower.remove(profile)
        profile.following.remove(follower)
        profile.following_n -= 1
        follower.follower_n -= 1
        follower.save()
        profile.save()
        return follower
    
  
        

    """