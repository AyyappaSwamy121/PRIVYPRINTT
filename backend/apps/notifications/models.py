from django.conf import settings
from django.db import models


class Notification(models.Model):
    class Category(models.TextChoices):
        SYSTEM = "system", "System"
        SECURITY = "security", "Security"
        SHARE = "share", "Share"
        PRINT = "print", "Print"
        VERIFICATION = "verification", "Verification"

    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications",
    )
    title = models.CharField(max_length=255)
    message = models.TextField()
    category = models.CharField(
        max_length=24,
        choices=Category.choices,
        default=Category.SYSTEM,
    )
    payload = models.JSONField(default=dict, blank=True)
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["recipient", "is_read", "created_at"]),
            models.Index(fields=["category", "created_at"]),
        ]

    def __str__(self) -> str:
        return f"Notification<{self.recipient_id}:{self.category}>"
