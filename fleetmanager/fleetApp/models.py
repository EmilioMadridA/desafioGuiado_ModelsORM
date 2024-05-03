from django.db import models
from django.db.models import PROTECT
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.
class Driver(models.Model):
    rut = models.CharField(max_length=9, primary_key=True, verbose_name=_("RUT"))
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name=_("Name"))
    last_name = models.CharField(max_length=50, null=False, blank=False, verbose_name=_("Last Name"))
    active = models.BooleanField(default=False, verbose_name=_("Active"))
    created_at = models.DateTimeField(default=timezone.now, verbose_name=_("Created At"))
    vehicle = models.OneToOneField("Vehicle", related_name="driver", null=True, blank=True, on_delete=models.PROTECT, verbose_name=_("Vehicle"))

    def __str__(self):
        return self.rut

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"
        ordering = ["rut"]


class Vehicle(models.Model):
    registration_plate = models.CharField(max_length=6, primary_key=True, verbose_name=_("Registration Plate"))
    brand = models.CharField(max_length=20, null=False, blank=False, verbose_name=_("Brand"))
    model = models.CharField(max_length=20, null=False, blank=False, verbose_name=_("Model"))
    year = models.DateField(null=False, blank=False, verbose_name=_("Year"))
    active = models.BooleanField(default=False, verbose_name=_("Active"))
    created_at = models.DateTimeField(default=timezone.now, verbose_name=_("Created At"))

    def __str__(self):
        return self.registration_plate

    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"
        ordering = ["registration_plate"]


class AccountingRecord(models.Model):
    purchase_date = models.DateField(null=False, blank=False, verbose_name=_("Purchase Date"))
    price = models.FloatField(null=False, blank=False, verbose_name=_("Price"))
    vehicle = models.OneToOneField("Vehicle", related_name="contabilidad", on_delete=PROTECT, verbose_name=_("Vehicle"))

    def __str__(self):
        return self.vehicle.registration_plate

    class Meta:
        verbose_name = "Accounting Record"
        verbose_name_plural = "Accounting Records"
        ordering = ["purchase_date"]