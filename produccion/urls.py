from django.urls import path
from produccion import views

urlpatterns = [
    path('manager/', views.manager, name='manager'),
    #path('produccion/gestion_materiales/', views.gestion_materiales, name='gestion_materiales'),  # Nueva URL
]
