from django.urls import path
from . import views 

urlpatterns = [
    path('', views.main),
    path('peliculas/', views.peliculas),
    path('param/<str:username>', views.hola)
]