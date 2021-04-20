from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.permissions import IsAuthenticated

from booking.models import Halls
from booking.serializers import HallSerializer


class HallListCreateViews(generics.GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = HallSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Halls.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class HallRetrieveUpdateEditView(generics.GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = HallSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Halls.objects.prefetch_related('hall_bookings').all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
