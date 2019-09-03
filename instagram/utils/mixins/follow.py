from rest_framework.response import Response
from rest_framework.decorators import action
from users.serializers import UserSerializer ,ProfileSerializer ,FollowerSerializer
from users.models import Profile


class Follow(object):
    @action (methods=['post'] ,detail = False)
    def follow(self, request ):
        
        user = request.user
        profile= Profile.objects.get(user=user)
        serializer = FollowerSerializer(profile,data=request.data)

        serializer.is_valid(raise_exception=True)


        follower = Profile.objects.get(id=request.data['follower'])
        follower.followers.add(profile)
        profile.following.add(follower)
        profile.following_n += 1
        follower.followers_n += 1
        follower.save()
        profile.save()
        return Response(ProfileSerializer(profile).data , 200)

