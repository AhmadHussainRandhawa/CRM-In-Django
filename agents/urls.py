from django.urls import path
from .views import AgentListView, AgentCreateView, AgentDetailView, AgentEditView, AgentDeleteView

app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name='agentList'),
    path('create/', AgentCreateView.as_view(), name='agentCreate'),
    path('<int:pk>/detail/', AgentDetailView.as_view(), name='agentDetail'),
    path('<int:pk>/edit/', AgentEditView.as_view(), name='agentEdit'),
    path('<int:pk>/delete/', AgentDeleteView.as_view(), name='agentDelete'),
    
]
