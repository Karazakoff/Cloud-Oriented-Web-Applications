from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from .serializers import RegisterUserSerializer, UserDetailsSerializer, UpdateUserSerializer, ChangePasswordSerializer
from .models import User
from .permissions import IsAuthor


class RegisterUserView(APIView):
    @swagger_auto_schema(request_body=RegisterUserSerializer())
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Вы успешно зарегистрировались", status=201)

class DetailsUserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, email=None):
        if email is None:
            email = request.user.email
        user = get_object_or_404(User, email=email)
        return Response(UserDetailsSerializer(user).data)

class UpdateUserView(APIView):
    permission_classes = [IsAuthenticated, IsAuthor]

    @swagger_auto_schema(request_body=UpdateUserSerializer())
    def patch(self, request):
        serializer = UpdateUserSerializer(request.user, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=201)

class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated, IsAuthor]

    def delete(self, request):
        request.user.delete()
        return Response(status=204)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated, IsAuthor]

    @swagger_auto_schema(request_body=ChangePasswordSerializer())
    def patch(self, request):
        serializer = ChangePasswordSerializer(request.user, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response(status=201)