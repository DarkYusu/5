"""facturas_proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from facturas_aplicacion.views import (FacturaListView, FacturaCreateView, FacturaUpdateView, FacturaDeleteView,DetalleFacturaListView, DetalleFacturaCreateView, DetalleFacturaUpdateView, DetalleFacturaDeleteView,index, SignupView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignupView.as_view(), name='signup'),
    path('', index, name='index'),
    path('facturas/', FacturaListView.as_view(), name='factura_list'),
    path('facturas/create/', FacturaCreateView.as_view(), name='factura_create'),
    path('facturas/<int:pk>/update/', FacturaUpdateView.as_view(), name='factura_update'),
    path('facturas/<int:pk>/delete/', FacturaDeleteView.as_view(), name='factura_delete'),
    path('facturas/<int:factura_id>/detalles/', DetalleFacturaListView.as_view(), name='detalle_factura_list'),
    path('facturas/<int:factura_id>/detalles/create/', DetalleFacturaCreateView.as_view(), name='detalle_factura_create'),
    path('detalles/<int:pk>/update/', DetalleFacturaUpdateView.as_view(), name='detalle_factura_update'),
    path('detalles/<int:pk>/delete/', DetalleFacturaDeleteView.as_view(), name='detalle_factura_delete'),
]
