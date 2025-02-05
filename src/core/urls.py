from django.contrib import admin
from django.urls import path
from auth import views as authViews
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', authViews.login_view, name='login'),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
]
