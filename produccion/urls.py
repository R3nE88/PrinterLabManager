from django.urls import path
from produccion.views.manager import manager

urlpatterns = [
    path('manager/', manager, name='manager'),
    #path('produccion/gestion_materiales/', views.gestion_materiales, name='gestion_materiales'),  # Nueva URL
]
