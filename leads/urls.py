from django.urls import path
from . import views

app_name = 'leads'
urlpatterns = [
    path('', views.leadList, name='leadList'),
    path('<int:pk>/', views.leadDetail, name='leadDetail'),
    path('create/', views.leadCreate, name='leadCreate'),
    path('<int:pk>/edit/', views.leadEdit, name='leadEdit'),
    path('<int:pk>/delete/', views.leadDelete, name='leadDelete')
]