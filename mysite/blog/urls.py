# blog/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'blog'  # ✅ Enables {% url 'blog:list' %}

urlpatterns = [
    path('', views.post_list, name='list'),  # ✅ This must exist
    path('<int:pk>/', views.post_detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
