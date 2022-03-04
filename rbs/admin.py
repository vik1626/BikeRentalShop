from django.contrib import admin
from .models import Customer,VehicleInventory,RentalMaster
# Register your models here.

admin.site.register(Customer)
# admin.site.register(VehicleInventory)
admin.site.register(RentalMaster)

@admin.register(VehicleInventory)
class VehicleInventoryAdmin(admin.ModelAdmin):
    list_display = ['id','vehicle_type','inventory_stock','email_id']