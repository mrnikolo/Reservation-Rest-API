from django.urls import path
from hotel.views import HotelListView, ReserveListCreate, RoomListCreateView

app_name = 'hotel'
urlpatterns = [
    path('', HotelListView.as_view(), name='hotel_list'),
    path('reserve', ReserveListCreate.as_view(), name='reserve_create_list_view'),
    path('room', RoomListCreateView.as_view(), name='room_create_list_view'),
]
