from rest_framework import serializers

from booking.models import Halls, HallBookings


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Halls
        fields = '__all__'


class HallBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallBookings
        fields = '__all__'
        extra_kwargs = {
            'user_id': {'required': False, 'read_only': True},
            'hall_id': {'required': False, 'read_only': True}
        }

    def create(self, validated_data):
        hall_id = self.context.get('hall_id', None)
        user_id = self.context.get('user_id', None)
        validated_data['hall_id'] = hall_id
        validated_data['user_id'] = user_id

        return super().create(validated_data)

    def update(self, instance, validated_data):
        hall_id = self.context.get('hall_id', None)
        user_id = self.context.get('user_id', None)
        validated_data['hall_id'] = hall_id
        validated_data['user_id'] = user_id

        return super().update(instance, validated_data)
