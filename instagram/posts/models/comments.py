from django.db import models
from utils.abstract_model import AbstractModel

class Comment(AbstractModel):
    """
    Este es el modelo de comentarios es un modelo con una relacion
    recursiva, el perfil y reply son atributos a tener en cuenta
    """
    #perfil del usuario que comenta relacion muchos a uno
    profile = models.ForeignKey(to='users.Profile' , on_delete =models.CASCADE)
    # reply es el campo no requerido y recursivo
    reply = models.ManyToManyField(to='posts.Comment' , related_name='reply_comments' , blank=True)
    like = models.PositiveIntegerField(default=0)
    #contenido del comentario
    text = models.TextField()
