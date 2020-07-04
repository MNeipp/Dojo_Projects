from django.urls import path
from . import views
from login_app import views as login_views

urlpatterns=[
    path('', views.index, name="home"),
    path('shop', views.shop, name='shop'),
    path('shop/show/<int:product_id>',views.product_info, name='product_info'),
    path('cart', views.cart, name="cart"),
    path('logout/', login_views.logout, name="logout"),

]