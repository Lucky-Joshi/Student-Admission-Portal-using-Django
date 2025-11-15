from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('form/', views.registration_form, name='form'),
    path('success/', views.success, name='success'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]
