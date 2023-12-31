from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    # path('post_list/', views.post_list, name='post_list'),
    path('crear_posteo/', views.crear_posteo, name='crear_posteo'),
    path('modificar_posteo/<id>/', views.modificar_posteo, name='modificar_posteo'),
    path('eliminar_posteo/<id>/', views.eliminar_posteo, name='eliminar_posteo'),
    path('post_list/', PostListView.as_view(), name='post_list'),
]
