from django.urls import path
from . import views

app_name = 'leads'
urlpatterns = [
    path('', views.LeadListView.as_view(), name='leadList'),
    path('create/', views.LeadCreateView.as_view(), name='leadCreate'),
    path('<int:pk>/detail', views.LeadDetailView.as_view(), name='leadDetail'),
    path('<int:pk>/edit/', views.LeadEditView.as_view(), name='leadEdit'),
    path('<int:pk>/delete/', views.LeadDeleteView.as_view(), name='leadDelete'),
    path('<int:pk>/assign-agent/', views.AssignAgentView.as_view(), name='assignAgent'),
    path('category/', views.CategoryListView.as_view(), name='categoryList'),
    path('category/detai/<int:pk>/', views.CategoryDetailView.as_view(), name='categoryDetail'),
    path('category/update/<int:pk>/', views.LeadCategoryUpdateView.as_view(), name='leadCategoryUpdate'),

]