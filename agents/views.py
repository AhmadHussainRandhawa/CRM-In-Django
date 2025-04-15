from django.shortcuts import reverse
from django.views import generic
from leads.models import Agent
from .forms import AgentModelForm

class AgentListView(generic.ListView):
    template_name = 'agents/agentList.html'
    context_object_name = 'agents'

    def get_queryset(self):
        return Agent.objects.all()
    
class AgentCreateView(generic.CreateView):
    template_name = 'agents/agentCreate.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agentList')
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
        return super().form_valid(form)
    
