from django.db import models

# Create your models here.

class Customer(models.Model):
    cust_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15,null=True, blank=True)
    email_id = models.CharField(max_length=50,null=True, blank=True)
    def __str__(self):
        return self.cust_name

    class Meta:
        db_table = 'rbs_customer'
    

class VehicleInventory(models.Model):
    vehicle_type = models.CharField(max_length=50)
    inventory_stock = models.IntegerField(default=0)
    email_id = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return self.vehicle_type
    class Meta:
        db_table = 'rbs_vehicle_inventory'

class RentalMaster(models.Model):
    rental_date = models.CharField(max_length=30,null=True, blank=True)
    return_date = models.CharField(max_length=30,null=True, blank=True)
    customer = models.ForeignKey(Customer, related_name='user_rental_master', null=True,
                             on_delete=models.CASCADE)
    vehicle = models.ForeignKey(VehicleInventory, related_name='user_vehicle_inventory', null=True,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.cust_name +self.vehicle.vehicle_type

    class Meta:
        db_table = 'rbs_rental_master'
