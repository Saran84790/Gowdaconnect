from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('directory/', views.directory, name='directory'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),

    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),

]

