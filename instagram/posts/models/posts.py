from django.db import models
from utils.abstract_model import AbstractModel


class Post(AbstractModel):
    """
        model for posts 
    """
    profile = models.ForeignKey('users.Profile',
     help_text = 'este es una clave foranea diciendo que los posts pueden tener muchos usuarios'
     , on_delete=models.CASCADE)

    photo = models.ImageField(
        upload_to = 'static/posts' 
        , blank=True)

    photobase64 = models.TextField( blank=True)
    description = models.CharField(max_length=255)
    #indicadores de likes y comentarios son una variable numerica para hacerle la vida facil al front
    likes = models.IntegerField(default=0)
    reply = models.IntegerField(default=0)
    #los comentarios pueden ser vacios osea no tener comentarios
    comments = models.ManyToManyField(
        to='posts.Comment' , 
        blank=True)
