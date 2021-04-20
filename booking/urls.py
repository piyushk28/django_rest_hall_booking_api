from django.urls import path

from booking.views import HallListCreateViews, HallRetrieveUpdateEditView

urlpatterns = [
    path('halls/', HallListCreateViews.as_view(), name='UpdateMyProfile'),
    path('halls/<int:pk>/', HallRetrieveUpdateEditView.as_view(), name='MyAddressCreateUpdateEditView'),

]
