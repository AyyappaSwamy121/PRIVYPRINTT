from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class PrintJob(models.Model):
    class Status(models.TextChoices):
        QUEUED = "queued", "Queued"
        PROCESSING = "processing", "Processing"
        COMPLETED = "completed", "Completed"
        FAILED = "failed", "Failed"
        CANCELLED = "cancelled", "Cancelled"

    class Mode(models.TextChoices):
        BW = "bw", "Black & White"
        COLOR = "color", "Color"

    document = models.ForeignKey(
        "vault.VaultDocument",
        on_delete=models.CASCADE,
        related_name="print_jobs",
    )
    requested_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="print_jobs",
    )
    print_shop = models.ForeignKey(
        "print_shops.PrintShop",
        on_delete=models.SET_NULL,
        related_name="print_jobs",
        null=True,
        blank=True,
    )
    copies = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    page_range = models.CharField(max_length=64, blank=True)
    print_mode = models.CharField(max_length=8, choices=Mode.choices, default=Mode.BW)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.QUEUED)
    failure_reason = models.TextField(blank=True)
    scheduled_for = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["status", "scheduled_for"]),
            models.Index(fields=["requested_by", "created_at"]),
        ]

    def __str__(self) -> str:
        return f"PrintJob<{self.id}:{self.status}>"
