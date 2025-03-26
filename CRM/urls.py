from django.contrib import admin
from django.urls import path, include
from leads.views import homePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace='leads')),
    path('', homePage, name='homePage'),

    path("__reload__/", include("django_browser_reload.urls")),

]
