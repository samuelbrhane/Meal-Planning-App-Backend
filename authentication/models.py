from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

# Define user groups
class UserGroups:
    USER_GROUP_NAME = 'User'
    SUPERUSER_GROUP_NAME = 'Superuser'

    @staticmethod
    def create_groups():
        user_group, created = Group.objects.get_or_create(name=UserGroups.USER_GROUP_NAME)
        superuser_group, created = Group.objects.get_or_create(name=UserGroups.SUPERUSER_GROUP_NAME)


class UserAccountManager(BaseUserManager):
    # create a new user account
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        
        user.set_password(password)
        user.save()
        
        # add user to User group
        user.groups.add(Group.objects.get(name=UserGroups.USER_GROUP_NAME))
        return user
    
    # create a new super user account
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        # create superuser object
        superuser = self.create_user(email, password, **extra_fields)
        
        # add superuser to Superuser group
        superuser.groups.add(Group.objects.get(name=UserGroups.SUPERUSER_GROUP_NAME))
        
        return superuser
 
    
    
class UserAccount(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    meal_type = models.CharField(max_length=255, blank=True, null=True)
    allergies = models.JSONField(default=list, blank=True)
    groups = models.ManyToManyField(Group, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    
    objects = UserAccountManager()
    
    def get_full_name(self):
        return self.first_name + " " + self.last_name
    
    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email
    
class TokenBlacklist(models.Model):
    """
    A model to store blacklisted tokens. This is useful for logout functionality.
    """
    token = models.CharField(max_length=500, unique=True)
    blacklisted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Token Blacklist"
        verbose_name_plural = "Token Blacklist"

class OutstandingToken(models.Model):
    """
    A model to store outstanding tokens. These are tokens that have not expired yet but
    have been deleted or blacklisted manually.
    """
    token = models.CharField(max_length=500, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Outstanding Token"
        verbose_name_plural = "Outstanding Tokens"

   