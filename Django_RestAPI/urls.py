# Import the necessary modules for the Django admin and URL handling
from django.contrib import admin
from django.urls import path, include

# Define the URL patterns for your Django project
urlpatterns = [
    # URL pattern for the Django admin interface
    path('admin/', admin.site.urls),

    # URL pattern for including URLs from an 'api' app
    path('api/', include('api.urls')),

    # URL pattern for including URLs from a 'pharmacy' app
    path('pharmacy/', include('pharmacy.urls')),
]

# 1.The first URL pattern (path('admin/', admin.site.urls)) maps the '/admin/' URL to the Django admin interface. This is where you can manage your Django project's administration.

# 2.The second URL pattern (path('api/', include('api.urls'))) includes URLs from an app named 'api'. This is typically used for defining API endpoints.

# 3.The third URL pattern (path('pharmacy/', include('pharmacy.urls'))) includes URLs from an app named 'pharmacy'. This is useful for routing requests related to a pharmacy section of your project.

# 4.These URL patterns allow you to structure the routing of URLs within your Django project and can help organize different parts of your application.
