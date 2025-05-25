from __future__ import unicode_literals
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="E-Posta",
        unique=True
    )
    first_name = models.CharField(
        verbose_name="Ad",
        max_length=30,
        blank=True
    )
    last_name = models.CharField(
        verbose_name="Soyad",
        max_length=30,
        blank=True
    )
    date_joined = models.DateTimeField(
        verbose_name="Katılma Tarihi",
        auto_now_add=True
    )
    is_active = models.BooleanField(
        verbose_name="Aktif Mi?",
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name="Yetkili Mi?",
        default=False,
        help_text="Kullanıcının bu yönetici sitesine giriş yapıp yapamayacağını belirtir",
    )
    avatar = models.ImageField(
        upload_to="avatars/",
        null=True,
        blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def get_full_name(self):
        """
        Ad ve soyadını aralarında bir boşluk olacak şekilde döndürür.
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    def get_short_name(self):
        """
        Kullanıcının kısa adını döndürür.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Bu kullanıcıya bir e-posta gönderir.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
