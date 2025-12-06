from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Home page (static template view)
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # Include app routes
    path('services/', include('services.urls')),
    path('bookings/', include('bookings.urls')),
    path('users/', include('users.urls')),
]

# Media file serving (for development)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
