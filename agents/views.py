from django.shortcuts import reverse
from django.views import generic
from leads.models import Agent
from .forms import AgentModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import OrganizationAndLoginRequiredMixin
from django.core.mail import send_mail


class AgentListView(OrganizationAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/agentList.html'
    context_object_name = 'agents'

    def get_queryset(self):
        return Agent.objects.filter(organization=self.request.user.userprofile)
    

class AgentDetailView(OrganizationAndLoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agentDetail.html'
    context_object_name = 'agent'

    def get_queryset(self):
        return Agent.objects.filter(organization=self.request.user.userprofile)


class AgentCreateView(OrganizationAndLoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agentCreate.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agentList')
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_organizer = False
        user.is_agent = True
        user.save()
        
        Agent.objects.create(user=user, organization=self.request.user.userprofile)

        send_mail(
            subject='Welcome to CRM',
            message='You have been added as an agent. Login to continue',
            from_email='admin@gmail.com',
            recipient_list=[user.email],)

        return super().form_valid(form)
    

class AgentEditView(OrganizationAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agentEdit.html'
    context_object_name = 'agent'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agentList')
    
    def get_queryset(self):
        return Agent.objects.filter(organization=self.request.user.userprofile)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object().user
        return kwargs


class AgentDeleteView(OrganizationAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/agentDelete.html'

    def get_success_url(self):
        return reverse('agents:agentList')

    def get_queryset(self):
        return Agent.objects.filter(organization=self.request.user.userprofile)