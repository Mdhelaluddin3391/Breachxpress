from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('exposes/', views.exposes, name='exposes'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('submit-story/', views.submit_story, name='submit_story'),
    path('community/', views.community, name='community'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('tag/<slug:slug>/', views.tag_detail, name='tag_detail'),
    path('terms_conditions', views.terms_conditions, name='terms_conditions'),
    path('privacy/', views.privacy, name='privacy'),
  
    
]