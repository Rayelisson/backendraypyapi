from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_crete_view),
    path('<int:pk>/', views.ProductDetailAPIView.as_view())
]
