from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index_file"),
    path('all_customer/', views.get_all_customer, name="get_all_customer"),
    path('add_customer/', views.add_customer, name="add_customer"),
    path('all_inventory/', views.get_all_inventory, name="all_inventory"),
    path('add_inventory/', views.add_inventory, name="add_inventory"),
    path('all_rental_bookings/', views.get_all_rental_bookings, name="all_rental_bookings"),
    path('add_rental_booking/', views.add_rental_booking, name="add_rental_booking"),
    # path('emp_details/<int:user_id>/', views.get_emp_details, name="emp_details"),
]
