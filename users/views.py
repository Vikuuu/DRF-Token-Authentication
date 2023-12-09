from rest_framework.response import Response
from .serializers import UserProfileSerializer
from rest_framework.views import APIView
from .models import UserProfile
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user

        profile = UserProfile.objects.get(user=user)
        profile_serializer = UserProfileSerializer(profile, many=False)

        return Response(
            {"profile": profile_serializer.data, "user": str(user.username)}
        )

    def put(self, request, format=None):
        user = self.request.user
        data = request.data

        serializer = UserProfileSerializer(data=data)

        if not serializer.is_valid():
            return Response({"error": serializer.errors})

        first_name = serializer.validated_data["first_name"]
        last_name = serializer.validated_data["last_name"]
        phone_no = serializer.validated_data["phone_no"]

        user = User.objects.get(id=user.id)

        UserProfile.objects.filter(user=user).update(
            first_name=first_name, last_name=last_name, phone_no=phone_no
        )

        user_profile = UserProfile.objects.get(user=user)
        serializer = UserProfileSerializer(user_profile)

        return Response({"profile": serializer.data, "username": str(user.username)})
