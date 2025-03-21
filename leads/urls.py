from django.urls import path
from . import views

app_name = 'leads'
urlpatterns = [
    path('', views.leadList, name='leadList'),
    path('<int:pk>/', views.leadDetail, name='leadDetail'),

]