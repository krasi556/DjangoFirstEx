from django.urls import path

from people import views

urlpatterns = [
    path('people/', views.employees_info,name='people')
]