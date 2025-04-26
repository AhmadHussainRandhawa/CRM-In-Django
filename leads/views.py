from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Lead, Category
from .forms import LeadModelForm, CustomeUserCreationForm, AssignAgentForm, LeadCategoryUpdateForm
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


class AssignAgentView(OrganizationAndLoginRequiredMixin, generic.FormView):
    form_class = AssignAgentForm
    template_name = 'leads/assignAgent.html'

    def get_success_url(self):
        return reverse('leads:leadList')

    def get_form_kwargs(self, **kwargs):
        kwargs = super().get_form_kwargs(**kwargs)
        kwargs.update({'request': self.request})
        return kwargs
    
    def form_valid(self, form):
        agent = form.cleaned_data['agent']
        lead = Lead.objects.get(id=self.kwargs['pk'])
        lead.agent = agent
        lead.save()
        return super().form_valid(form)      


class CategoryListView(LoginRequiredMixin, generic.ListView):
    template_name = 'leads/categoryList.html'
    context_object_name = 'categories'
    
    def get_queryset(self):
        
        if self.request.user.is_organizer:
            queryset = Category.objects.filter(organization=self.request.user.userprofile)
        else:
            queryset = Category.objects.filter(organization=self.request.user.agent.organization)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile, category__isnull=True).count()
            context.update({'unassigned_leads_count': queryset})
        return context
    

class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'leads/categoryDetail.html'
    context_object_name = 'category'

    def get_queryset(self):
        user = self.request.user
        
        if user.is_organizer:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            queryset = Category.objects.filter(organization=user.agent.organization)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        leads = self.get_object().lead_set.all()  # Lead.objects.filter(category=self.get_object())
        context.update({'leads':leads})
        return context


class LeadCategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'leads/leadCategoryUpdate.html'
    form_class = LeadCategoryUpdateForm

    def get_queryset(self):
        user = self.request.user

        if user.is_organizer:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            queryset = Category.objects.filter(organization=user.agent.organization)
            queryset = queryset.filter(agent__user=user)
    
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add this line (you're in a Category update view, so you likely need to fetch the related lead manually)
        context["lead"] = self.object.lead_set.first()  # or any other logic that fits your design

        return context

    def get_success_url(self):
        return reverse('leads:leadDetail', kwargs={"pk":self.get_object().id})
    

# Function based views:

"""def homePage(request):
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
        form = leadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leads:leadList')
        
    else: 
        form = leadModelForm()
    
    context = {'form':form}
    return render(request, 'leads/leadCreate.html', context)
    
def leadEdit(request, pk):
    lead = Lead.objects.get(id=pk)
    if request.method=='POST':
        form = leadModelForm(request.POST, instance=lead)   # It add new data in the previous lead
        if form.is_valid():
            form.save()
            return redirect('leads:leadList')
    else: 
        form = leadModelForm(instance=lead)     # It shows the previous data of a lead
    
    context = {'form':form, 'lead':lead}
    return render(request, 'leads/leadEdit.html', context)
    

def leadDelete(pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('leads:leadList')
"""


"""def leadEdit(request, pk):
    lead = Lead.objects.get(id=pk)
    if request.method=='POST':
        form = leadModelForm(request.POST)
        if form.is_valid():
            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = form.cleaned_data['agent']

            lead.first_name = first
            lead.last_name = last
            lead.age = age
            lead.agent = agent

            lead.save()
            return redirect('leads:leadList')

    else: 
        form = leadModelForm(request.POST)
    
    context = {'lead':lead, 'form': form}
    
    return render(request, 'leads/leadEdit.html', context)


def leadCreate(request):
    if request.method=="POST":
        form = leadForm(request.POST)
        if form.is_valid():
            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.get(id=2)
            Lead.objects.create(first_name=first, last_name=last, age=age, agent=agent)
            return redirect('leads:leadList')
                
    else:
        form = leadForm()

    context = {'form': form}

    return render(request, 'leads/leadCreate.html', context)
"""