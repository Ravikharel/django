from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignUpView.as_view, name='signup'),
    # path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),\
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('profile/', views.profile, name='profile'),
    path('create-post/',views.create_post, name='create_post'),

]