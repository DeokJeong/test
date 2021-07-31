from rest_framework.serializers import ModelSerializer
from .models import Todo



class TodoSerializer(ModelSerializer):

    class Meta:
        model = Todo
        fields = ["id", "title", "content", "created_at", "modified_at"]