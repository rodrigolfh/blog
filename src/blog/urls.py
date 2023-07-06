from django.urls import path
from . import views

urlpatterns = [
    path('post_list/', views.post_list, name='post_list'),
    path('crear_posteo/', views.crear_posteo, name='crear_posteo'),
    path('modificar_posteo/<id>/', views.modificar_posteo, name='modificar_posteo'),
]
