from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from .models import Lead
from .forms import LeadModelForm, CustomeUserCreationForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganizationAndLoginRequiredMixin

# Class Based Views
class HomePageView(generic.TemplateView):
    template_name = 'homePage.html'


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = 'leads/leadList.html'
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile, agent__isnull=False)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
            # Filter for the agent that is logged in.
            queryset = queryset.filter(agent__user=user)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile, agent__isnull=True)
            context.update({'unassigned_leads': queryset})
        
        return context


    



class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'leads/leadDetail.html'
    context_object_name = 'lead'

    def get_queryset(self):
        if self.request.user.is_organizer:
            queryset = Lead.objects.filter(organization=self.request.user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=self.request.user.agent.organization)
            # Filter for the agent that is logged in.
            queryset = queryset.filter(agent__user=self.request.user)
        return queryset


class LeadCreateView(OrganizationAndLoginRequiredMixin, generic.CreateView):
    template_name = 'leads/leadCreate.html'
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse ('leads:leadList')
    
    def form_valid(self, form):
        send_mail(
            subject='A lead is created',
            message="Go and check the new leads",
            from_email='officialtest',
            recipient_list=["i don't kniw test" 'maybe serius hojaye']
        )
        return super().form_valid(form)


class LeadEditView(OrganizationAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'leads/leadEdit.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    context_object_name = 'lead'

    def get_success_url(self):
        return reverse('leads:leadList')

    def get_queryset(self):
        return  Lead.objects.filter(organization=self.request.user.userprofile)

        
class LeadDeleteView(OrganizationAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'leads/leadDelete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:leadList')

    def get_queryset(self):
        return  Lead.objects.filter(organization=self.request.user.userprofile)


class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomeUserCreationForm

    def get_success_url(self):
        return reverse('login')



# Function based views:
"""
def homePage(request):
    return render(request, 'homePage.html')

def leadList(request):
    leads = Lead.objects.all()
    context = {'leads': leads}

    return render(request, 'leads/leadList.html', context)

def leadDetail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {'lead': lead}

    return render(request, 'leads/leadDetail.html', context)

def leadCreate(request):
    if request.method=='POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leads:leadList')
        
    else: 
        form = LeadModelForm()
    
    context = {'form':form}
    return render(request, 'leads/leadCreate.html', context)
    
def leadEdit(request, pk):
    lead = Lead.objects.get(id=pk)
    if request.method=='POST':
        form = LeadModelForm(request.POST, instance=lead)   # It add new data in the previous lead
        if form.is_valid():
            form.save()
            return redirect('leads:leadList')
    else: 
        form = LeadModelForm(instance=lead)     # It shows the previous data of a lead
    
    context = {'form':form, 'lead':lead}
    return render(request, 'leads/leadEdit.html', context)
    

def leadDelete(pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('leads:leadList')"""
