from users.views import UserViewset ,ProfileViewset , ProfileViewsetDetail
from rest_framework.routers import SimpleRouter
from django.contrib import admin
from django.urls import path , include

router = SimpleRouter()
router.register(r'user' , UserViewset, basename='users')
router.register(r'profile', ProfileViewset,basename='profile')
router.register(r'profile/(?P<id>[0-9]+)/detail', ProfileViewsetDetail,basename='profile')



urlpatterns = [
    path('',include(router.urls))
]