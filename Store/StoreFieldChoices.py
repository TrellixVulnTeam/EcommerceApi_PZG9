from django.db import models


class Size(models.TextChoices):
        SMALL = "S"
        MEDIUM = "M"
        LARGE = "L"