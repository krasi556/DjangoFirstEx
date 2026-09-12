from django.urls import path

from address import views

urlpatterns = [
    path('address/', views.show_address, name='address')
]
