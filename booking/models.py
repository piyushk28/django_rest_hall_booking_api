from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q

from utils.datetime_parser import convert_str_to_datetime
from utils.mixins import CreatedByUpdateByMixin

User = get_user_model()


class Halls(models.Model, CreatedByUpdateByMixin):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    capacity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    @classmethod
    def get_availability_query(cls, start, end):
        filter_query = Q(hall_bookings__start__range=(start, end)) | Q(hall_bookings__end__range=(start, end)) | Q(
            Q(hall_bookings__start__lte=start, hall_bookings__end__gte=start) & Q(hall_bookings__start__lte=end,
                                                                                  hall_bookings__end__gte=end))

        return filter_query

    def check_availability(self, start, end):
        start = convert_str_to_datetime(start)
        end = convert_str_to_datetime(end)
        filter_query = Q(start__range=(start, end)) | Q(end__range=(start, end)) | Q(
            Q(start__lte=start, end__gte=start) & Q(start__lte=end, end__gte=end))

        qs = self.hall_bookings.filter(filter_query)
        return not qs.exists()


class HallBookings(models.Model, CreatedByUpdateByMixin):
    hall_id = models.ForeignKey(Halls, on_delete=models.CASCADE, related_name='hall_bookings')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hall_bookings')
    start = models.DateTimeField(verbose_name="Booking Start DateTime")
    end = models.DateTimeField(verbose_name="Booking End DateTime")

    def __str__(self):
        name = f"{self.start} - {self.end}"
        if self.hall_id:
            name = f"{self.hall_id.name}( {self.start} - {self.end})"
        return name
