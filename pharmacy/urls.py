from django.urls import path
from . import views

urlpatterns = [
    path('new/user', views.new_user),
    path('user/login', views.login_view),
    path('user/logout', views.logout_view),
    path('amb/booking', views.book),
    # Add other URLs here
]
