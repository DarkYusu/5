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
from django.contrib.auth.decorators import login_required
from facturas_aplicacion.views import (FacturaListView, EmpresaListView, ReceptorListView, FacturaCreateView, FacturaUpdateView, FacturaDeleteView,DetalleFacturaListView, DetalleFacturaCreateView, DetalleFacturaUpdateView, DetalleFacturaDeleteView, EmpresaCreateView, EmpresaUpdateView,EmpresaDeleteView,ReceptorCreateView,ReceptorUpdateView,ReceptorDeleteView, index, SignupView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignupView.as_view(), name='signup'),
    path('', index, name='index'),
    path('facturas/', login_required(FacturaListView.as_view()), name='factura_list'),
    path('facturas/create/', login_required(FacturaCreateView.as_view()), name='factura_create'),
    path('facturas/<int:pk>/update/', login_required(FacturaUpdateView.as_view()), name='factura_update'),
    path('facturas/<int:pk>/delete/', login_required(FacturaDeleteView.as_view()), name='factura_delete'),
    path('facturas/<int:factura_id>/detalles/', login_required(DetalleFacturaListView.as_view()), name='detalle_factura_list'),
    path('facturas/<int:factura_id>/detalles/create/', login_required(DetalleFacturaCreateView.as_view()), name='detalle_factura_create'),
    path('detalles/<int:pk>/update/', login_required(DetalleFacturaUpdateView.as_view()), name='detalle_factura_update'),
    path('detalles/<int:pk>/delete/', login_required(DetalleFacturaDeleteView.as_view()), name='detalle_factura_delete'),
    
    path('empresas/', login_required(EmpresaListView.as_view()), name='empresa_list'),
    path('empresas/create/', login_required(EmpresaCreateView.as_view()), name='empresa_create'),
    path('empresas/<int:pk>/update/', login_required(EmpresaUpdateView.as_view()), name='empresa_update'),
    path('empresas/<int:pk>/delete/', login_required(EmpresaDeleteView.as_view()), name='empresa_delete'),
    
    path('receptores/', login_required(ReceptorListView.as_view()), name='receptor_list'),
    path('receptores/create/', login_required(ReceptorCreateView.as_view()), name='receptor_create'),
    path('receptores/<int:pk>/update/', login_required(ReceptorUpdateView.as_view()), name='receptor_update'),
    path('receptores/<int:pk>/delete/', login_required(ReceptorDeleteView.as_view()), name='receptor_delete'),
]
