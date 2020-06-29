from django.shortcuts import render

from .models import *
# Create your views here.

def profile(request):
    profiles=Profile.objects.all()
    context={
        'profiles':profiles,
    }
    return render(request,"Profile/profile.html",context)