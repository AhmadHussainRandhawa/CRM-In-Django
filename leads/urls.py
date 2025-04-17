from django.urls import path
from . import views

app_name = 'leads'
urlpatterns = [
    path('', views.LeadListView.as_view(), name='leadList'),
    path('<int:pk>/detail', views.LeadDetailView.as_view(), name='leadDetail'),
    path('create/', views.LeadCreateView.as_view(), name='leadCreate'),
    path('<int:pk>/edit/', views.LeadEditView.as_view(), name='leadEdit'),
    path('<int:pk>/delete/', views.LeadDeleteView.as_view(), name='leadDelete')
]