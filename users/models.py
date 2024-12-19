from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from django.core.validators import RegexValidator

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255),
    phonenumber = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^(05|06|07|03)\d{8}$',
                message='Enter a valid number',
                code='invalid_registration',
            )
        ]
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name','last_name','phonenumber']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
