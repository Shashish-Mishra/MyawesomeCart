from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('products/<int:myid>',views.productview,name='productview'),
    path('contact',views.contact,name='contact'),
    path('checkout',views.checkout,name='checkout'),
    path('tracker/',views.tracker,name='tracker'),
    path('search/',views.search,name='search'),
    path('handlerequest/',views.handlerequest,name='handlerequest'),
]