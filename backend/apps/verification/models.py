import uuid

from django.conf import settings
from django.db import models


class IdentityVerification(models.Model):
    class VerificationType(models.TextChoices):
        EMAIL = "email", "Email"
        PHONE = "phone", "Phone"
        ID_DOCUMENT = "id_document", "ID Document"
        FACE = "face", "Face Match"

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        VERIFIED = "verified", "Verified"
        REJECTED = "rejected", "Rejected"
        EXPIRED = "expired", "Expired"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="verifications",
    )
    verification_type = models.CharField(max_length=24, choices=VerificationType.choices)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.PENDING)
    reference_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    verified_value = models.CharField(max_length=255, blank=True)
    requested_at = models.DateTimeField(auto_now_add=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    rejection_reason = models.TextField(blank=True)

    class Meta:
        ordering = ["-requested_at"]
        indexes = [
            models.Index(fields=["user", "status"]),
            models.Index(fields=["verification_type", "status"]),
        ]

    def __str__(self) -> str:
        return f"Verification<{self.user_id}:{self.verification_type}:{self.status}>"
