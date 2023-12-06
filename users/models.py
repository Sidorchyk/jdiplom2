from django.core.mail import send_mail
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
    )
    phone = models.CharField(max_length=12, unique=True)
    telegram_id = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone', 'telegram_id']
    objects = UserManager()

    def __str__(self):
        return self.telegram_id

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, phone, username, telegram_id, password, **extra_fields):
        """
        Create and save a user with the given username, email,
        full_name, and password.
        """
        if not phone:
            raise ValueError('The given phone must be set')
        if not username:
            raise ValueError('The given username must be set')
        if not telegram_id:
            raise ValueError('The given telegram_id must be set')

        phone = self.normalize_phone(phone)
        username = self.model.normalize_username(username)
        telegram_id = self.model.normalize_telegram_id(telegram_id)
        user = self.model(
            phone=phone, username=username, telegram_id=telegram_id,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        # user.save(using=self._db)
        return user
    def create_user(self, phone, username, telegram_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            phone, username, telegram_id, password, **extra_fields
        )
    def create_superuser(self, phone, username, telegram_id, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(
            phone, username, telegram_id, password, **extra_fields
        )