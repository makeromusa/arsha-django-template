from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('starter/', views.starter, name='starter'),
    path('services/details/', views.service_details, name='service_details'),
    path('portfolio/details/', views.portfolio_details, name='portfolio_details'),
    path('blog/', views.blog, name='blog'),
    path('blog/details/', views.blog_details, name='blog_details'),
    path('contact/', views.contact_view, name='contact'),
    path('newsletter/', views.newsletter_view, name='newsletter'),
    path('404/', views.custom_404_view, name='custom_404_view'),
]
