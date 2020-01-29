from django.urls import path
from .views import profile, update_profile

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('update/', update_profile, name='update-profile')
]