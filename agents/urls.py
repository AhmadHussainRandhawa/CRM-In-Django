from django.urls import path
from .views import AgentListView, AgentCreateView, AgentDetailView, AgentEditView, AgentDeleteView

app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name='agentList'),
    path('create/', AgentCreateView.as_view(), name='agentCreate'),
    path('detail/<int:pk>/', AgentDetailView.as_view(), name='agentDetail'),
    path('edit/<int:pk>/', AgentEditView.as_view(), name='agentEdit'),
    path('delete/<int:pk>/', AgentDeleteView.as_view(), name='agentDelete'),
    
]
