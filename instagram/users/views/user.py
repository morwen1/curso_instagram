from rest_framework import viewsets , mixins 
from users.models import User ,Profile
from users.serializers import UserSerializer ,register_Serializer, ProfileSerializer,FollowerSerializer
from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework.status import HTTP_201_CREATED , HTTP_200_OK
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny , IsAuthenticated , IsAuthenticatedOrReadOnly

from utils.mixins.follow import Follow

class UserViewset(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet,
                   Follow):
    queryset = User.objects.filter(is_active = True)
    serializer_class = UserSerializer

    def get_permissions (self):
        permisions = []
        if self.action in ['list', 'retrieve']:
            permisions = [AllowAny, IsAuthenticatedOrReadOnly]
        if self.action == 'profile':
            permisions = [IsAuthenticated]
        if self.action in ['login' , 'register']:
            permisions= [AllowAny]
        return [p() for p in permisions]

    @action (methods=['post'] , detail=False)
    def register(self, request):
        serializer = register_Serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user=serializer.save()
        data= UserSerializer(user).data
        return Response (data , status=HTTP_201_CREATED)
    
    
    @action(methods=['post'] , detail = False)
    def login(self, request):
        serializer = TokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data  , status=200)

    @action(methods=['post' , 'patch' , 'put'] , detail = False)
    def profile(self, request ):
        user = request.user
        profile = Profile.objects.get(user=user)
        partial = request.method == 'PATCH'
        serializer = ProfileSerializer(profile, data=request.data , partial =partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=200)
    
    

    
