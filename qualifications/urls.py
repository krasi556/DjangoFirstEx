from django.urls import path

from qualifications import views

urlpatterns = [
    path('qualification/', views.show_qualifications, name='qualifications')
]
