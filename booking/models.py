from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q

from booking.enums import HallStatusEnum
from utils.mixins import CreatedByUpdateByMixin

User = get_user_model()


class Halls(models.Model, CreatedByUpdateByMixin):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    capacity = models.PositiveIntegerField(default=0)

    def check_availability(self, start, end):
        filter_query = Q(
            status__in=(HallStatusEnum.PENDING.value, HallStatusEnum.COMPLETED.value, HallStatusEnum.PROGRESS.value))

        filter_query &= Q(start__gte=start) | Q(end__lte=start) | Q(start__gte=end) | Q(end__lte=end)

        qs = self.hall_bookings.filter(filter_query)

        if qs.exists():
            return False
        return True


class HallBookings(models.Model, CreatedByUpdateByMixin):
    hall_id = models.ForeignKey(Halls, on_delete=models.CASCADE, related_name='hall_bookings')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hall_bookings')
    start = models.DateTimeField(verbose_name="Booking Start DateTime")
    end = models.DateTimeField(verbose_name="Booking End DateTime")
    status = models.CharField(max_length=50,
                              choices=HallStatusEnum.choices(),
                              default=HallStatusEnum.PENDING.value)
