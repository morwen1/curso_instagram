#django
from django.urls import path , include
#rest framework
from rest_framework.routers import SimpleRouter

#local views
from posts.views import PostfeedViewset

router = SimpleRouter( )
router.register(r'feed', PostfeedViewset , basename='feedpost' )

urlpatterns = [
    path('',include(router.urls))
]