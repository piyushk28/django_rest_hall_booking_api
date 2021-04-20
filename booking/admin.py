from django.contrib import admin

# Register your models here.
from booking.models import Halls, HallBookings

admin.site.register(Halls)
admin.site.register(HallBookings)