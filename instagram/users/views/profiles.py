from rest_framework import viewsets  
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from django.db.models import Q

from users.models import Profile 
from posts.models import Post
from users.serializers import ProfileSerializer
from posts.serializers import PostSerializer
from utils.mixins import Follow


class ProfileViewset(Follow,
                	viewsets.mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    
    queryset = Profile.objects.filter(
            Q(user__is_active = True)
          
    )
    serializer_class = ProfileSerializer



class ProfileViewsetDetail(	Follow,
							viewsets.mixins.ListModelMixin,
							viewsets.GenericViewSet):
	def dispatch(self,request, *args , **kwargs):
		self.id_profile_detail = kwargs['id']
		self.profile = get_object_or_404(Profile, id=self.id_profile_detail)
		return super(ProfileViewsetDetail, self ).dispatch(request,*args , **kwargs)

	def get_queryset(self):
		queryset = Profile.objects.filter(id=self.profile.id)
		return queryset

	
	serializer_class=ProfileSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]

	@action(methods=['get'] , detail=False)
	def posts(self , data , *args , **kwargs):
		posts = Post.objects.filter(profile=self.profile)
		serializer = PostSerializer(posts , allow_null=True , many=True)
		return Response(serializer.data)

		
