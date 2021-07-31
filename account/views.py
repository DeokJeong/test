from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import UserSerializer



class RegisterView(APIView):
    def post(self, request):
        username = request.data.get("username", None)
        password1 = request.data.get("password1", None)
        password2 = request.data.get("password2", None)

        if not username or not password1 or not password2:
            return Response({"content": "Required Parameter", "error": True}, status=status.HTTP_400_BAD_REQUEST)

        if password1 != password2:
            return Response({"content": "password1 and password2 mismatch", "error": True}, status=status.HTTP_400_BAD_REQUEST)
        
        u = User(username=username)
        u.set_password(password1)
        u.save()

        return Response({"content": "Success", "error": False}, status=status.HTTP_201_CREATED)


class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request, pk=None):
        if request.user.is_superuser:
            if not pk:
                u = User.objects.all()
                users = UserSerializer(u, many=True)
            else:
                try:
                    u = User.objects.filter(pk=pk)[0]
                except:
                    return Response({"content": "Invalid User ID", "error": True}, status=status.HTTP_400_BAD_REQUEST)

                users = UserSerializer(u)
        else:
            u = User.objects.filter(pk=request.user.pk)[0]
            users = UserSerializer(u)

        return Response({"content": users.data, "error": False}, status=status.HTTP_200_OK)
    
    def put(self, request, pk=None):
        if request.user.is_superuser:
            if not pk:
                return Response({"content": "Required User ID", "error": True}, status=status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    u = User.objects.filter(pk=pk)[0]
                except:
                    return Response({"content": "Invalid User ID", "error": True}, status=status.HTTP_400_BAD_REQUEST)
        else:
            u = User.objects.filter(pk=request.user.pk)[0]
        
        password1 = request.data.get("password1", None)
        password2 = request.data.get("password2", None)

        if password1 != password2:
            return Response({"content": "password1 and password2 mismatch", "error": True}, status=status.HTTP_400_BAD_REQUEST)
        
        u.set_password(password1)
        u.save()
        
        return Response({"content": "Success", "error": False}, status=status.HTTP_205_RESET_CONTENT)
    
    def delete(self, request, pk=None):
        permission_classes = [permissions.IsAdminUser,]

        if request.user.is_superuser:
            if not pk:
                return Response({"content": "Required User ID", "error": True}, status=status.HTTP_400_BAD_REQUEST)

            try:
                u = User.objects.filter(pk=pk)
                u.delete()

                return Response({"content": "Success", "error": False}, status=status.HTTP_204_NO_CONTENT)
            except:
                return Response({"content": "Invalid User ID", "error": True}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"content": "Admin Required", "error": True}, status=status.HTTP_400_BAD_REQUEST)




