from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/', views.staff,name='dashboard-staff'),
    path('staff/detail/<int:pk>', views.staff_detail,name='dashboard-staff-detail'),
    path('supplier/', views.supplier,name='dashboard-supplier'),
    path('supplier/delete/<int:pk>/', views.supplier_delete,name='dashboard-supplier-delete'),
    path('supplier/update/<int:pk>/', views.supplier_update,name='dashboard-supplier-update'),
    path('product/', views.product,name='dashboard-product'),
    path('product/delete/<int:pk>/', views.product_delete,name='dashboard-product-delete'),
    path('product/update/<int:pk>/', views.product_update,name='dashboard-product-update'),
    path('order/', views.order,name='dashboard-order'),
]