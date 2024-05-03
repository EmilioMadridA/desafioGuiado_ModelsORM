from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import Driver, Vehicle, AccountingRecord

# Register your models here.
@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    exclude = ('created_at',)
    actions = ["export_to_csv"]

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="drivers.csv"'
        writer = csv.writer(response)
        writer.writerow(["RUT", "Name", "Last Name", "Active", "Created At", "Vehicle"])
        for driver in queryset:
            writer.writerow(
                [
                    driver.rut,
                    driver.name,
                    driver.last_name,
                    driver.active,
                    driver.created_at,
                    driver.vehicle,
                ]
            )
        return response

    export_to_csv.short_description = "Export selected drivers to CSV"


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    exclude = ('created_at',)
    actions = ["export_to_csv"]

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="vehicles.csv"'
        writer = csv.writer(response)
        writer.writerow(
            ["Registration Plate", "Brand", "Model", "Year", "Active", "Created At"]
        )
        for vehicle in queryset:
            writer.writerow(
                [
                    vehicle.registration_plate,
                    vehicle.brand,
                    vehicle.model,
                    vehicle.year,
                    vehicle.active,
                    vehicle.created_at,
                ]
            )
        return response

    export_to_csv.short_description = "Export selected vehicles to CSV"


@admin.register(AccountingRecord)
class AccountingRecordAdmin(admin.ModelAdmin):
    actions = ["export_to_csv"]

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = (
            'attachment; filename="accountingrecords.csv"'
        )
        writer = csv.writer(response)
        writer.writerow(["Purchase Date", "Price", "Vehicle"])
        for accounting_registry in queryset:
            writer.writerow(
                [
                    accounting_registry.purchase_date,
                    accounting_registry.price,
                    accounting_registry.vehicle,
                ]
            )
        return response

    export_to_csv.short_description = "Export selected accounting registries to CSV"