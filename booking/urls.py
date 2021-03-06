from django.urls import path

from booking.views import HallListCreateViews, HallRetrieveUpdateEditView, HallBookingListCreateView, \
    AvailableHallView, BookingListView

urlpatterns = [
    path('halls/', HallListCreateViews.as_view(), name='HallListCreateViews'),
    path('halls/available/', AvailableHallView.as_view(), name='AvailableHallView'),
    path('halls/<int:pk>/', HallRetrieveUpdateEditView.as_view(), name='HallRetrieveUpdateEditView'),
    path('halls/bookings/', BookingListView.as_view(), name='BookingListView'),
    path('halls/<int:hall_id>/booking/', HallBookingListCreateView.as_view(), name='HallBookingListCreateView'),

]
