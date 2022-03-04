from urllib import response
from django.shortcuts import render
from .models import Customer, RentalMaster, VehicleInventory
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request ,'index.html')


def get_all_customer(request,emp_records=None):
    if emp_records:
        customer_records=emp_records
    else:
        customer_records = Customer.objects.all()
    records = {
        "data":customer_records
    }
    return render(request ,'customer.html',records)

def get_all_inventory(request,inv_records=None):
    if inv_records:
        inventory_records=inv_records
    else:
        inventory_records = VehicleInventory.objects.all()
    records = {
        "data":inventory_records
    }
    return render(request ,'inventory.html',records)

def get_all_rental_bookings(request,booking_records=None):
    if booking_records:
        rental_booking_records=booking_records
    else:
        rental_booking_records = RentalMaster.objects.all()
    records = {
        "data":rental_booking_records
    }
    return render(request ,'rental_booking.html',records)


def add_customer(request):
    if request.method=='GET':
        return render(request ,'add_customer.html')
    elif request.method=='POST':
        customer_name = request.POST['customer_name']
        contact_no = request.POST['contact_no']
        email_id = request.POST['email_id']
        emp_obj = Customer(cust_name=customer_name,contact_number=contact_no,email_id=email_id)
        emp_obj.save()
        return get_all_customer(request)

def add_inventory(request):
    if request.method=='GET':
        return render(request ,'add_inventory.html')
    elif request.method=='POST':
        vehicle_type = request.POST['vehicle_type']
        inventory_stock = request.POST['inventory_stock']
        vehicle_obj = VehicleInventory.objects.filter(vehicle_type__iexact=vehicle_type).order_by('-id').first()
        if vehicle_obj:
           vehicle_obj.inventory_stock =inventory_stock
           vehicle_obj.save()
        else:
            vehicle_obj = VehicleInventory(vehicle_type=vehicle_type,inventory_stock=inventory_stock)
            vehicle_obj.save()
        return get_all_inventory(request)

def add_rental_booking(request):
    if request.method=='GET':
        customer_records = Customer.objects.all()
        vehicle_records = VehicleInventory.objects.all()
        records = {
            "data":customer_records,
            "vehicle_data":vehicle_records
        }
        return render(request ,'add_rental_booking.html',records)
    elif request.method=='POST':
        customer = request.POST['customer']
        vehicle_type = request.POST['vehicle_type']
        rental_date = request.POST['rental_date']
        return_date = request.POST['return_date']
        customer_obj = Customer.objects.filter(cust_name=customer).order_by('-id').first()
        vehicle_obj = VehicleInventory.objects.filter(vehicle_type=vehicle_type).order_by('-id').first()
        if not vehicle_obj.inventory_stock:
            records = {
                "msg":f"{vehicle_obj.vehicle_type}cannot be rented as it is already booked"
            }
            return render(request ,'Error_screen.html',records)

        emp_obj = RentalMaster(customer=customer_obj,
                rental_date=rental_date,
                return_date=return_date,
                vehicle=vehicle_obj,)
        emp_obj.save()
        vehicle_obj.inventory_stock-=1
        vehicle_obj.save()
        return get_all_rental_bookings(request)