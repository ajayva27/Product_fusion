from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Organization, Member, Role 
from .serializers import UserSerializer, OrganizationSerializer, MemberSerializer, RoleSerializer
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.http import HttpResponse
import logging

def home_view(request):
    return HttpResponse("Welcome to the API")


# SignUp 
class SignUpView(APIView):
    def post(self, request):
        user_data = request.data.copy()  
        user_data['password'] = make_password(user_data['password'])
        user_serializer = UserSerializer(data=user_data)

        if user_serializer.is_valid():
            user = user_serializer.save()


            organization_data = {
                'name': request.data.get('organization_name'),
                'status': 1,
                'personal': False,
                'settings': {}
            }
            org_serializer = OrganizationSerializer(data=organization_data)

            if org_serializer.is_valid():
                org = org_serializer.save()

                owner_role = Role.objects.create(name="Owner", description="Organization Owner", org_id=org)

                Member.objects.create(user=user, org=org, role=owner_role)

            return Response(user_serializer.data, status=status.HTTP_201_CREATED)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# SignIn

logger = logging.getLogger(__name__)

class SignInView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"detail": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        user = authenticate(username=user.username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
