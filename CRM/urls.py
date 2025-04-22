from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from leads.views import HomePageView, SignupView
from django.contrib.auth.views import (
    LoginView, 
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView, 
    PasswordResetCompleteView,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace='leads')),
    path('agents/', include('agents.urls', namespace='agents')),
    path('', HomePageView.as_view(), name='homePage'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', SignupView.as_view(), name='signup'),
    path('password-reset', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path("__reload__/", include("django_browser_reload.urls")),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
