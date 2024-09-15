from rest_framework import serializers
from .models import User, Organization, Role, Member
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'profile', 'status', 'settings', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True},  
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  
        return super(UserSerializer, self).create(validated_data)


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['name', 'status', 'personal', 'settings', 'created_at', 'updated_at']
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }


class RoleSerializer(serializers.ModelSerializer):
    organization = serializers.CharField(source='org_id.name', read_only=True)  

    class Meta:
        model = Role
        fields = ['name', 'description', 'org_id', 'organization']


class MemberSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user_id.email', read_only=True)  
    organization = serializers.CharField(source='org_id.name', read_only=True)  
    role = serializers.CharField(source='role_id.name', read_only=True)  

    class Meta:
        model = Member
        fields = ['org_id', 'user_id', 'role_id', 'status', 'settings', 'created_at', 'updated_at', 'user', 'organization', 'role']
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
