from django.urls import path
from . import views


app_name = 'poorly_coded_store'

urlpatterns = [
    path('', views.index),
    path('checkout/<int:quantity>/<int:price>/', views.checkout, name='checkout'),
    path('pay', views.pay, name='pay')
]
