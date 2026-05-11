from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('donate/', views.donate, name='donate'),
    path('campaign/', views.campaign, name='campaign'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('donatehistory/', views.donatehistory, name='donatehistory'),
    path('formdonate/', views.formdonate, name='formdonate'),
]