from django.utils.translation import gettext_lazy as _
from django.db import models

class Status(models.TextChoices):
    NEW= "NEW", _("Novo")
    CANCELLED = "CAN", _("Cancelado")
    WARNING = "WAR", _("Alerta")
    READY = "REA", _("Pronto")
    FINISHED = "FIN", _("Finalizado")
