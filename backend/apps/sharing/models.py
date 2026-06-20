import uuid

from django.conf import settings
from django.db import models


class DocumentShare(models.Model):
    class AccessLevel(models.TextChoices):
        VIEW = "view", "View"
        COMMENT = "comment", "Comment"
        DOWNLOAD = "download", "Download"
        PRINT = "print", "Print"

    document = models.ForeignKey(
        "vault.VaultDocument",
        on_delete=models.CASCADE,
        related_name="shares",
    )
    shared_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="outgoing_shares",
    )
    shared_with = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="incoming_shares",
        null=True,
        blank=True,
    )
    shared_with_email = models.EmailField(blank=True)
    access_level = models.CharField(
        max_length=16,
        choices=AccessLevel.choices,
        default=AccessLevel.VIEW,
    )
    access_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    revoked_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["document", "access_level"]),
            models.Index(fields=["shared_with", "revoked_at"]),
        ]

    def __str__(self) -> str:
        return f"Share<{self.document_id}:{self.access_level}>"
