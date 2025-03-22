from django.shortcuts import render, redirect
from .models import Lead, Agent
from .forms import LeadForm


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
        form = LeadForm(request.POST)
        if form.is_valid():
            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            dob = form.cleaned_data['date_of_birth']
            agent = Agent.objects.get(id=2)

            Lead.objects.create(first_name=first, last_name=last, date_of_birth=dob, agent=agent)
            return redirect('leads:leadList')
        
    else: 
        form = LeadForm()

    context = {'form': form}

    return render(request, 'leads/leadCreate.html', context)


def leadEdit(request, pk):
    lead = Lead.objects.get(id=pk)
    if request.method=='POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            dob = form.cleaned_data['date_of_birth']
            agent = Agent.objects.get(id=1)

            lead.first_name=first
            lead.last_name = last
            lead.date_of_birth = dob
            lead.agent = agent
            lead.save()
            return redirect('leads:leadList')

    else: 
        form = LeadForm()

    context = {'form': form}    
    return render(request, 'leads/leadEdit.html', context)

def leadDelete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('leads:leadList')