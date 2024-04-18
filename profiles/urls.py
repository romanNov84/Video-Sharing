from django.urls import path
from .views import ProfileView, UpdateProfile
from . import views


urlpatterns = [
    path('<int:pk>/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/update/', UpdateProfile.as_view(), name='update-profile'),
    path('delete_profile.html/', views.delete_profile, name='delete-profile'),
    path('delete-profile/<str:username>/', views.delete_user_profile, name='delete_user_profile'),
]
