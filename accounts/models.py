from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

# User Roles
USER_ROLES = (
    ('client', 'client'),
    ('driver', 'driver'),
    ('admin', 'driver'),
)

#Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, full_name, phone, password=None, role='client'):
        """ Create and return a regular user"""
        if not email:
            raise ValueError('An email address is required')
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, phone=phone, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user 

    def create_superuser(self, email, full_name, phone, password=None):
        """ create and return a super user """
        user = self.create_user(
            email=email,
            full_name=full_name,
            phone=phone,
            password=password,
            role='admin'
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

#Custom user model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='client')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone']

    def __str__(self):
        return f"{self.full_name} ({self.role})"


# Driver Profile

class Driver(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='driver_profile')
    license_number = models.CharField(max_length=50)
    national_id  = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=50, default='Car')
    rating = models.FloatField(default=5.0)
    is_available = models.BooleanField(default=True)
    experience_years = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Driver: {self.user.full_name}"

#Admin Profile
class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='admin_profile')

    def __str__(sefl):
        return f"Admin: {self.user.full_name}"