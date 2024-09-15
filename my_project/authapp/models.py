from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class Organization(models.Model):
    name = models.CharField(max_length=255, null=False)
    status = models.IntegerField(default=0, null=False)
    personal = models.BooleanField(default=False, null=True)
    settings = models.JSONField(default=dict, null=True)
    created_at = models.BigIntegerField(null=True)
    updated_at = models.BigIntegerField(null=True)

class Role(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            profile={},
            created_at=int(timezone.now().timestamp())
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    profile = models.JSONField(default=dict, null=False)
    status = models.IntegerField(default=0, null=False)
    settings = models.JSONField(default=dict, null=True)
    created_at = models.BigIntegerField(null=True)
    updated_at = models.BigIntegerField(null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Member(models.Model):
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    status = models.IntegerField(default=0, null=False)
    settings = models.JSONField(default=dict, null=True)
    created_at = models.BigIntegerField(null=True)
    updated_at = models.BigIntegerField(null=True)
