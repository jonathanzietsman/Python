from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# The urlpatterns list routes URLs to views.
# This is the main URL configuration for the entire Django project.
urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the Django admin panel (e.g., /admin/)
    
    # Includes Django's built-in authentication views like login, logout, password reset
    path('accounts/', include('django.contrib.auth.urls')),

    # Includes the URL patterns defined in the 'reci_app' application
    # This means the homepage and other URLs handled by reci_app will be routed from here
    path('', include('reci_app.urls')),
]

# This part is only used during development (when DEBUG=True)
# It allows media files (like uploaded images) to be served properly by Django's development server
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
