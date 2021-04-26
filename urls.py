from django.urls import path

from . import views 

app_name = 'shop'

urlpatterns = [
    path('', views.all_products, name = 'all_products'),
    path('login', views.login_page, name = 'login_page'),
    path('pants', views.pants_page, name = 'pants_page'),
    path('shirts', views.shirts_page, name = 'shirts_page'),
    path('tshirts', views.tshirts_page, name = 'tshirts_page'),
    path('sweaters', views.sweaters_page, name = 'sweaters_page'),
    path('item/<slug:slug>/', views.product_detail , name= 'product_detail'),
    path('search/<slug:category_slug>/', views.category_list , name= 'category_list'),
]
