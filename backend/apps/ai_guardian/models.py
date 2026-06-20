from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class DocumentRiskAssessment(models.Model):
    class RiskLevel(models.TextChoices):
        LOW = "low", "Low"
        MEDIUM = "medium", "Medium"
        HIGH = "high", "High"
        CRITICAL = "critical", "Critical"

    document = models.OneToOneField(
        "vault.VaultDocument",
        on_delete=models.CASCADE,
        related_name="risk_assessment",
    )
    scanned_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="risk_assessments",
        null=True,
        blank=True,
    )
    risk_level = models.CharField(
        max_length=16,
        choices=RiskLevel.choices,
        default=RiskLevel.LOW,
    )
    score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0,
    )
    findings = models.JSONField(default=list, blank=True)
    recommendation = models.TextField(blank=True)
    scanned_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-scanned_at"]
        indexes = [
            models.Index(fields=["risk_level", "scanned_at"]),
        ]

    def __str__(self) -> str:
        return f"RiskAssessment<{self.document_id}:{self.risk_level}>"
