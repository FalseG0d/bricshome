from django.shortcuts import render,redirect

from Home.models import Report
from .forms import ReportForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .decorators import unauthenticated_user
# Create your views here.
@login_required(login_url='login')
def interface(request):
    form=ReportForm()
    if request.method=='POST':
        print("Post")
        form=ReportForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            print("Valid Form")
            content_form = form.save(commit=False)
            content_form.author = request.user
            content_form.save()

            return redirect('/')
        else:
            print("Invalid Form")
    
    print("Not Post Handling")
    context={
        'form':form,
    }
    return render(request,'ContentWriter/interface.html',context)


@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('interface')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'ContentWriter/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')
