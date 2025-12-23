from django.contrib import admin
from django.urls import path, include
from accounts.views import LandingView, RegisterView, LoginView, LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('accounts/', include('accounts.urls')),
    
    path('tasks/', include('tasks.urls')),
    
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'), 
    path('register/', RegisterView.as_view(), name='register'),

    path('', LandingView.as_view(), name='landing'),
]