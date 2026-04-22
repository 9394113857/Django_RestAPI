from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# simple root check
def home(request):
    return HttpResponse("Django API is LIVE 🚀")

urlpatterns = [
    path('', home),                       # root URL
    path('admin/', admin.site.urls),      # admin
    path('api/', include('api.urls')),   # api app
    path('pharmacy/', include('pharmacy.urls')),  # pharmacy app
]
