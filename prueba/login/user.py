from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, password):
        if not username:
            raise ValueError('User must have a username')
        if not first_name:
            raise ValueError('User must have a first_name')
        if not last_name:
            raise ValueError('User must have a last_name')
        if not email:
            raise ValueError('User must have an email address')
        if not password:
            raise ValueError('User must have a password')
        
        user = self.model(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = self.normalize_email(email),
        )
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, username, first_name, last_name, email, password):
        user = self.model(
            username = username,
            first_name = first_name,
            last_name = last_name, 
            password = password,
            email = self.normalize_email(email),
        )
        
        user.is_staff = True
        user.save(using=self._db)
        
        
class User(AbstractBaseUser):
    US_NORMAL = 1
    US_ADMIN = 2
    
    ROL = (
        (US_NORMAL, 'Usuario normal'),
        (US_ADMIN, 'Usuario administrador')
    )
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=9, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROL, blank=True)
    
    #required fields
    date_joined = models.DateTimeField()
    last_login = models.DateTimeField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superadmin= models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
