from django.shortcuts import render,redirect
from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home_page, name = 'home'),
    path('sobre-nosotros/',views.about_page, name = 'about'),
    path('servicios/',views.courses_page, name = 'services'),
    path('contacto/',views.contact_page, name = 'contact'),
    path('faq/',views.faq_page, name = 'faq'),
    path('blog',views.blog_page, name = 'blog'),
    path('politica-de-privacidad/',views.private_page,name='private'),
    path('terminos-y-condiciones/',views.terms_page, name = 'terms')
]
