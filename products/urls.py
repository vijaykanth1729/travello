from django.urls import path
from products.views import home, create,delete, detail, update, our_forum, demo_pic

app_name = 'products'
urlpatterns = [
    path('', home, name='home'),
    path('forum/', our_forum, name='forum'),
    path('products/create/', create, name='create'),
    path('products/<slug:slug>/delete/', delete, name='delete'),
    path('products/<slug:slug>/', detail, name='detail'),
    path('products/<slug:slug>/update/', update, name='update'),
    path('demo/', demo_pic, name='demo'),

]



#import products
# from products import home--->Best
# from products import *
# import products as p
