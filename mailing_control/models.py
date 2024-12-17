from django.db import models
from django.utils import timezone

from orders.models import Order


class Sent_email(models.Model):
    """Модель отправленных писем заказчику."""
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, related_name='sent_email'
    )
    sent = models.DateTimeField(blank=False, null=False, default=timezone.now)
