from django.urls import path
from . import views



app_name = 'ch'

urlpatterns = [
    path('',views.index,name='index'),
    path('add_room/',views.add_room,name='add_room'),
    path('checkview/',views.checkview,name='checkview'),
    path('send/',views.send,name='send'),
    path('<str:room>/',views.getMessages,name='getMessages'),
    path('<str:room>/',views.room,name='room'),
]