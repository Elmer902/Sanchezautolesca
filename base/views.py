from django.shortcuts import render
from .models import Messages
from django.contrib import messages
# Create your views here.

def home_page(request):
    return render(request,'index.html')

def about_page(request):
    return render(request,'about.html')

def blog_page(request):
    return render(request,'blog.html')

def contact_page(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        body = request.POST.get('body')
        
        message = Messages.objects.create(username=username, email=email,body=body)
        message.save() 
        messages.success(request, '¡Gracias por tu mensaje! Nos pondremos en contacto contigo lo antes posible.')   
    
    return render(request,'contact.html')

def faq_page(request):
    return render(request,'faq.html')

def courses_page(request):
    return render(request,'courses.html')


def private_page(request):
    return render(request,'privatepolicy.html')

def terms_page(request):
    return render(request,'Terms.html')