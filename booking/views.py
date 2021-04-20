from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from booking.models import Halls, HallBookings
from booking.serializers import HallSerializer, HallBookingSerializer

start_param = openapi.Parameter('start', openapi.IN_QUERY, required=True, description="Start DateTime",
                                type=openapi.TYPE_STRING)
end_param = openapi.Parameter('end', openapi.IN_QUERY, required=True, description="End DateTime",
                              type=openapi.TYPE_STRING)
capacity_param = openapi.Parameter('capacity', openapi.IN_QUERY, required=True, description="Capacity",
                                   type=openapi.TYPE_INTEGER)


class HallListCreateViews(generics.GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = HallSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Halls.objects.all().order_by('-capacity')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class HallRetrieveUpdateEditView(generics.GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = HallSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Halls.objects.prefetch_related('hall_bookings').all().order_by('-capacity')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AvailableHallView(generics.GenericAPIView, ListModelMixin):
    serializer_class = HallSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Halls.objects.prefetch_related('hall_bookings').all().order_by('-capacity')

    def get_start_datetime(self, ):
        params = self.request.query_params
        start = params.get('start')
        if not start:
            raise ValueError("start query_param is required!!!")
        return start

    def get_end_datetime(self, ):
        params = self.request.query_params
        end = params.get('end')
        if not end:
            raise ValueError("end query_param is required!!!")
        return end

    def get_capacity(self, ):
        params = self.request.query_params
        capacity = params.get('capacity')
        if not capacity:
            raise ValueError("capacity query_param is required!!!")
        return capacity

    def filter_queryset(self, queryset):
        start = self.get_start_datetime()
        end = self.get_end_datetime()
        capacity = self.get_capacity()
        query = Halls.get_availability_query(start, end)
        return queryset.filter(capacity__gte=capacity, user_id=self.request.user).exclude(query)

    @swagger_auto_schema(manual_parameters=[start_param, end_param, capacity_param])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class HallBookingListCreateView(generics.GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = HallBookingSerializer
    permission_classes = (IsAuthenticated,)
    queryset = HallBookings.objects.select_related('hall_id').all().order_by('-end')

    lookup_field = 'hall_id'

    def filter_queryset(self, queryset):
        return queryset.filter(user_id=self.request.user)

    def get_hall_object(self):
        return get_object_or_404(Halls, pk=self.kwargs[self.lookup_field])

    def check_hall_availability(self, request):
        data = request.data
        available = self.get_hall_object().check_availability(data['start'], data['end'])
        if not available:
            raise ValueError("This Hall is already registered")

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            'hall_id': self.get_hall_object(),
            'user_id': self.request.user}
        )
        return context

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.check_hall_availability(request)  # Checking whether a hall is available or not!!!
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @swagger_auto_schema(request_body=HallBookingSerializer(), responses={201: HallBookingSerializer()})
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
