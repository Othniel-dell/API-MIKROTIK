from django.db import models

# Create your models here.

from routeros_ssh_connector import MikrotikDevice


#router = MikroTikDevice()

class Router(models.Model):
    Name = models.CharField(max_length=200)