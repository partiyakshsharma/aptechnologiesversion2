from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contactus', views.contactus, name='contactus'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/<int:id>/', views.portfolio_detail, name='portfolio_detail'),
    path('all-brands/', views.all_brands, name='all_brands'),
    path('privacypolicy', views.privacypolicy, name='privacypolicy'),
    path('Termsconditions', views.Termsconditions, name='Termsconditions'),
    path('chatbot/',  views.chatbot_view, name='chatbot'),
]


