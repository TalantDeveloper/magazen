from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('detail/<int:magazen_id>/', views.detail_view, name='detail'),
    path('about/', views.about, name='about'),
]
