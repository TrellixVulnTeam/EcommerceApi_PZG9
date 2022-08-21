from django.urls import path,include
from Store import views

urlpatterns = [
    path('products/',views.ProductsList.as_view(),name='product_list'),
    path('products/<int:pk>', views.ProductDetailsView.as_view(), name='product_details'),
]