from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutButton, name = 'logout'),
    path('register/', views.register, name = 'register'),
    
    path('', views.home, name = 'home'),
    path('room/<str:pk>/', views.room, name = 'room'),
    path('profile/<str:pk>', views.userprofile, name = 'profile'),
    
    path('create-room/', views.createRoom, name = 'create-room'),
    path('update-room/<str:pk>', views.UpdateRoom, name = 'update-room'),
    path('delete-room/<str:pk>', views.deleteRoom, name = 'delete-room'),
    path('delete-message/<str:pk>', views.deletemess, name = 'delete-message'),
    path('edit-user/', views.editUser, name = 'edit-user'),
    
]