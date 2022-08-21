from django.urls import path,include
from Store import views

urlpatterns = [
    path('hellomac/',views.hello_mac,name='hello_mac'),
    path('products/',views.ProductsListView.as_view(),name='product_list'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product_details'),
    path('customp/', views.ProductsCustom.as_view(), name='custom_p'),
    path('custompd/<int:product_id>', views.ProductCustomDetails.as_view(),name="custom_pd")
]