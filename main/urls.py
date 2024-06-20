from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.welcome, name='welcome'),

    path('detail/<int:magazen_id>/', views.detail_view, name='detail'),
    path('about/', views.about, name='about'),

    path('jurnal/', views.jurnals_view, name='jurnals'),
    path('jurnal/<int:jurnal_id>/', views.jurnal_view, name='jurnal'),

    path('gazeta/', views.gazetas_view, name='gazetas'),
    path('gazeta/<int:gazeta_id>/', views.gazeta_view, name='gazeta'),

    path('maqola/', views.maqolas_view, name='maqolas'),
    path('maqola/<int:maqola_id>/', views.maqola_view, name='maqola'),
]
