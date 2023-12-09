from rest_framework.response import Response
from .serializers import UserProfileSerializer
from rest_framework.views import APIView
from .models import UserProfile
from rest_framework.permissions import IsAuthenticated


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        user = request.user

        profile = UserProfile.objects.get(user=user)
        profile_serializer = UserProfileSerializer(profile, many=False)

        return Response(profile_serializer.data)

    def put(self, request, format=None):
        user = request.user
        data = request.data
        
        profile_data = UserProfile.objects.get(user=user)
        serializer = UserProfileSerializer(instance=profile_data, data=data)
        
        if not serializer.is_valid():
            return Response({"error": serializer.errors})
        
        serializer.save()
        return Response(serializer.data)
