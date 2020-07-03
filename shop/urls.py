from . import views
from django.urls import path
app_name = 'shop'


urlpatterns = [
    #path('', views.home,name='home'),
    path('home/', views.tag_list,name='home'),
    path('shop/', views.product_list, name='product_list'),
    path('shop/sale', views.product_sale, name='sale'),
    path('home/<slug:tags_slug>/', views.tag_list,
    name='product_list_by_tag'),
    path('<slug:category_slug>/', views.product_list,
    name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),




]