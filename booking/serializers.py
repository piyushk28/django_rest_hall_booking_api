from rest_framework import serializers

from booking.models import Halls, HallBookings


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Halls
        fields = '__all__'


class HallBookingSerializer(serializers.ModelSerializer):
    class Meta:
        models = HallBookings
        fields = '__all__'
        depth = 1
