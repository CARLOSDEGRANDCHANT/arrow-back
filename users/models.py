from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):
    """
    Abstract model for users.
    """
    
    ROLE_ADMIN = 'A'
    ROLE_AGENT = 'G'
    
    ROLE_CHOICES = [
        (ROLE_ADMIN, _('Administrador')),
        (ROLE_AGENT, _('Agente')),
    ]
    
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default=ROLE_AGENT)
    
    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')
        
    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"
    
    
class Agent(models.Model):
    """
    Class that extends the abstract User class towards Agent data.
    """
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
class Admin(models.Model):
    """
    Class that extends the abstract User class towards Admin data.
    """
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
class Aseguradora(models.Model):
    name = models.CharField(max_length=200)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name