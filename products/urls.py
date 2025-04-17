from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('products/<product>/<productid>', views.product_cat, name="productcat"),
    path('signup', views.signup, name="signup"),
] 

