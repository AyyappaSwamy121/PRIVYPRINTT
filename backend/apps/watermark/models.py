from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class WatermarkRule(models.Model):
    class Position(models.TextChoices):
        CENTER = "center", "Center"
        DIAGONAL = "diagonal", "Diagonal"
        HEADER = "header", "Header"
        FOOTER = "footer", "Footer"

    document = models.OneToOneField(
        "vault.VaultDocument",
        on_delete=models.CASCADE,
        related_name="watermark_rule",
    )
    text = models.CharField(max_length=255)
    opacity = models.PositiveSmallIntegerField(
        default=30,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
    )
    rotation = models.SmallIntegerField(
        default=-30,
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
    )
    position = models.CharField(
        max_length=16,
        choices=Position.choices,
        default=Position.DIAGONAL,
    )
    include_user_identity = models.BooleanField(default=True)
    include_timestamp = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self) -> str:
        return f"WatermarkRule<{self.document_id}>"
