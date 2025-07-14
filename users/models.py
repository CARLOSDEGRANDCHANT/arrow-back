from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):
    """
    Model for users.
    """
    
    ROLE_ADMIN = 'A'
    ROLE_AGENT = 'G'
    
    ROLE_CHOICES = [
        (ROLE_ADMIN, _('Administrador')),
        (ROLE_AGENT, _('Agente')),
    ]
    
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default=ROLE_LAWYER)
    
    
    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')
        
    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"