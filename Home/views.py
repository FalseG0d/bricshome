from django.shortcuts import render
from .models import *
import smtplib, ssl

# Create your views here.
def home(request):
    
    sliders=Slider.objects.all()
    event=Event.objects.all()[0]
    about=About.objects.all()[0]
    report=Report.objects.all()[0]
    videos=Video.objects.all()[:5]
    images=GalleryImage.objects.all()[:6]
    links=Link.objects.all()
    context={
        'sliders':sliders,
        'event':event,
        'about':about,
        'images':images,
        'links':links,
        'videos':videos,
        'report':report,
    }
    return render(request,"home/index.html",context)

def reports(request):
    reports=Report.objects.all()
    context={
        'reports':reports,
    }
    return render(request,"home/reports.html",context)

def report(request,pk):
    reports=Report.objects.get(id=pk)
    context={
        'report':reports,
    }
    return render(request,"home/report.html",context)

def event(request,pk):
    event=Event.objects.get(id=pk)
    context={
        'event':event,
    }
    return render(request,"home/event.html",context)


def about(request):
    about=About.objects.all()[0]
    context={
        'about':about,
    }
    return render(request,"home/about.html",context)


def history(request):
    about=About.objects.all()[0]
    context={
        'about':about,
    }
    return render(request,"home/history.html",context)

def events(request):
    events=Event.objects.all()
    context={
        'events':events,
    }
    return render(request,"home/events.html",context)

def mail(request):

    if request.method=='POST':
        name=request.POST['name']
        reciever_email=request.POST['email']
        sub=request.POST['subject']
        body="A message was sent to you by "+reciever_email+". It said: \n"+request.POST['body']

        about=About.objects.all()[0]
        
        sender_email=about.email
        password=about.password

        with smtplib.SMTP('smtp.gmail.com',587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            #Email must allow Secondary Applications
            smtp.login(sender_email,password)

            msg=f'Subject:{sub}\n\n{body}'
            smtp.sendmail('email',sender_email,msg)

            sub="Message Recieved By DarkLight"
            body='Dear '+name+', This is to notify that your message has been recieved by DarkLight Photography.'
            msg=f'Subject:{sub}\n\n{body}'
            
            smtp.sendmail('email',reciever_email,msg)
            
    return redirect('/')

def gallery(request):
    images=GalleryImage.objects.all()
    context={
        'images':images,
    }
    return render(request,"home/gallery.html",context)


def video(request):
    videos=Video.objects.all()
    context={
        'videos':videos,
    }
    return render(request,"home/videogallery.html",context)