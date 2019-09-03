#django
from django.db.models import Q
from django.db.models import Subquery

#rest framework
from rest_framework import mixins 
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response 
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter 
#local models and serializers 
from posts.models import Post
from posts.serializers import PostSerializerfirst , PostSerializer
from users.models import Profile



class PostfeedViewset (mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    
    def get_queryset(self):
        
        profile = Profile.objects.get(
            user = self.request.user
        )
        following = profile.following.all().values('id')
        queryset =Post.objects.filter(
            Q(profile_id__in=following)|Q(profile = profile)
        ).order_by('created')
        return queryset
    



    serializer_class = PostSerializer
    permission_classes =[IsAuthenticated]
    filter_backends = [OrderingFilter]


    def create(self, request ) : 
        profile = Profile.objects.get(user=request.user)
        post = Post.objects.create(profile = profile)
        serializer = PostSerializerfirst(post , data=request.data)
        serializer.is_valid(raise_exception=True)
        post=serializer.save()

        return Response(PostSerializer(post).data , status=201)

    @action(methods=['post'],detail=False)
    def comment(self , request):
        import pdb; pdb.set_trace()
        return Response(request.data , status=200)
