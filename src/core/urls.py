from django.contrib import admin
from django.urls import path, include
from auth import views as authViews
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', authViews.login_view, name='login'),
    path('register/', authViews.register_view, name='register'),    
    path('accounts/', include('allauth.urls')),    
    path('admin/', admin.site.urls),
]
