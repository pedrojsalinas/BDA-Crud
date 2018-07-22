from django.urls import path

from proyecto.views import *

urlpatterns = [
    path('victimas/', VictimaView.as_view(), name='victimas'),
    path('agresores/', AgresorView.as_view(), name='agresores'),
    path('relaciones/', RelacionView.as_view(), name='relaciones'),
    path('femicidios/', FemicidioView.as_view(), name='femicidios'),
    path('detalle-agresor/<int:id>/', AgresorDetalleView.as_view(), name='detalle-agresor'),
    path('detalle-victima/<int:id>/', VictimaDetalleView.as_view(), name='detalle-victima'),
    path('detalle-femicidio/<int:id>/', FemicidioDetalleView.as_view(), name='detalle-femicidio'),
    path('delete_agresor/<int:pk>/', AgresorDetalleView.eliminar, name='eliminar-agresor'),
    path('delete_victima/<int:pk>/', VictimaDetalleView.eliminar, name='eliminar-victima'),
    path('delete_femicidio/<int:pk>/', FemicidioDetalleView.eliminar, name='eliminar-femicidio'),
]
