from django.db import models
from django.conf import settings


class Customer(models.Model):

    STATUS_CHOICES = (
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
    )

    customer_code = models.CharField(
        max_length=20,
        unique=True
    )

    company_name = models.CharField(
        max_length=255
    )

    contact_person = models.CharField(
        max_length=255
    )

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=20
    )

    website = models.URLField(
        blank=True,
        null=True
    )

    industry = models.CharField(
        max_length=100
    )

    city = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=100
    )

    country = models.CharField(
        max_length=100
    )

    postal_code = models.CharField(
        max_length=20
    )

    address = models.TextField()

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="customers"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    is_deleted = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "customers"
        ordering = ["company_name"]

    def __str__(self):
        return self.company_name