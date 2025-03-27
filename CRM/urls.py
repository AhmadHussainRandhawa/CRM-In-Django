from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from leads.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace='leads')),
    path('', HomePageView.as_view(), name='homePage'),

    path("__reload__/", include("django_browser_reload.urls")),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
