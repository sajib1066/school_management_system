from django.urls import path
from . import views

urlpatterns = [
    path('', views.ViewStore, name='view-store'),
    path('category<name>', views.ViewStoreCategory, name='view-store-category'),
    path('item/<id>', views.ViewStoreItem, name='view-store-item'),
    path('add-item', views.AddStoreItem, name='add-store-item'),
    path('remove-item', views.remove_from_cart, name='remove-from-cart'), 
    path('add-store-categorry', views.AddStoreCategory, name='add-store-category'), 
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'), 
    path('checkout/', views.ViewCheckout, name='view-checkout'),
    path('order-summary', views.OrderSummary, name='order-summary')  
]