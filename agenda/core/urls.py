from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos),
    path('agenda/' , views.lista_eventos),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('agenda/evento/', views.evento),
    path('agenda/evento/submit', views.submit_evento),
    path('agenda/evento/delete/<int:id_evento>',views.delete_evento),
    
]
