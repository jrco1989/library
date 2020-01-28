from django.contrib import admin
from django.urls import path
from django.urls import include 
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    #path('', RedirectView.as_view(url='/catalog/', permanent=True)), #Add URL maps to redirect the base URL to our application
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)# Use static() to add url mapping to serve static files during development (only)




#path('catalog/', include('catalog.urls')), #use include ()to add paths from the catalog application
