from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserAccountSerializer, UserLoginSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()


class RegisterView(APIView):
    def post(self, request, format=None):
        try:
            data = request.data
            serializer = UserAccountSerializer(data=data)

            if not serializer.is_valid():
                return Response(
                    {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
                )

            user = serializer.create(serializer.validated_data)
            user = User.objects.get(email=serializer.data["email"])

            token, _ = Token.objects.get_or_create(user=user)
            user = UserAccountSerializer(user)

            return Response(
                {"user": user.data, "token": str(token)}, status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"error": "Something went wrong while registering the user" + str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class LoginView(APIView):
    def post(self, request, format=None):
        try:
            data = request.data
            serializer = UserLoginSerializer(data=data)

            if not serializer.is_valid():
                return Response(
                    {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
                )
            
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            
            user = authenticate(request, email=email, password=password)
            
            if user:
                token = Token.objects.get(user=user)
                return Response(
                    {"user": serializer.data, "token": str(token)},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"error": "Invalid email or password"},
                    status=status.HTTP_401_UNAUTHORIZED
                )

        except Exception as e:
            return Response(
                {"error": "Something went wrong while logging in " + str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ForgetPasswordView(APIView):
    def post(self, request, format=None):
        pass


class UserProfileView(APIView):
    def patch(self, request, format=None):
        pass
