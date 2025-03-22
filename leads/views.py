from django.shortcuts import render, redirect
from .models import Lead
from .forms import LeadFormModel


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
        form = LeadFormModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leads:leadList')
        
    else: 
        form = LeadFormModel()
    
    context = {'form':form}
    return render(request, 'leads/leadCreate.html', context)
    
def leadEdit(request, pk):
    lead = Lead.objects.get(id=pk)
    if request.method=='POST':
        form = LeadFormModel(request.POST, instance=lead)   # It add new data in the previous lead
        if form.is_valid():
            form.save()
            return redirect('leads:leadList')
    else: 
        form = LeadFormModel(instance=lead)     # It shows the previous data of a lead
    
    context = {'form':form}
    return render(request, 'leads/leadEdit.html', context)
    

def leadDelete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('leads:leadList')