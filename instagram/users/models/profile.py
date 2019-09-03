from django.db import models
from utils.abstract_model import AbstractModel


class Profile(AbstractModel):
    user = models.OneToOneField(to='users.User' , on_delete=models.CASCADE )
    
    picture = models.ImageField(verbose_name='addres_image' , upload_to='users_images/profile')
    picturebase64 = models.TextField()
    address = models.TextField()
    website = models.URLField()
    #seguidores
    followers = models.ManyToManyField(to = 'users.Profile' , related_name='followers_profile' , blank=True)
    #numero de seguidores
    followers_n= models.PositiveIntegerField(default=0)
    #seguidos o siguiendo
    following = models.ManyToManyField(to = 'users.Profile' , related_name='following_profile' , blank=True)
    #numero de seguidos o siguiendo
    following_n = models.PositiveIntegerField(default=0)
    phone_number = models.CharField(max_length = 11)
    biography =models.TextField()
    def __str__(self):
        return "profile {}".format(self.user.username)
