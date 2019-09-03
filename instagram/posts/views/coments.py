from rest_framework.viewsets import ModelViewSet
from users.models import Comment
from users.serializers import CommentSerializer


class ReplyViewset(ModelViewSet):
    """
        vista para comentar comentarios
    """
    queryset =Comment.objects.all()
    serializer_class = CommentSerializer

