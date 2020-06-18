from django.shortcuts import render
from Home.models import Report
from .forms import ReportForm

# Create your views here.
def interface(request):
    form=ReportForm()
    if request.method=='POST':
        form=ReportForm(request.POST)
        form.author=request.user
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context={
        'form':form,
    }
    return render(request,'ContentWriter/interface.html',context)