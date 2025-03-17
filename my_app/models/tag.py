from django.core.validators import MinLengthValidator

from .base_model import BaseModel
from django.db import models


class Tag(BaseModel):
    name = models.CharField(
        max_length=200, null=False, blank=False,
        validators=[MinLengthValidator(5)],
        help_text="Nome para a tag. Entre 5 e 200 caracteres.",
        verbose_name="Descrição",
    )

    def __str__(self):
        return self.name