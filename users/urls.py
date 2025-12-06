from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # ✅ New route added
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),  # ✅ Placeholder for next step
    path('signup/', views.signup_view, name='signup'),
]
