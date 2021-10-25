from django.urls import path
from chat import views

urlpatterns = [
    path('', views.index, name='index'),
    path('messages/<str:room>/', views.get_messages, name='get_messages'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.check_room, name='checkview'),
    path('send', views.send, name='send'),

]
