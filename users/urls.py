from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserCreate, ProfileUpdate, ProfileView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name = 'accounts/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('signup/', UserCreate.as_view(), name='signup'),

    path("profile/", ProfileView.as_view(), name="profile"),

    path('profile_update/', ProfileUpdate.as_view(), name='profile_update'),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name = 'accounts/reset_password.html'
    ), name='reset_password'),

    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]
