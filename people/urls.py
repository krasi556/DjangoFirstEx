from django.urls import path

from people import views

app_name = 'people'
urlpatterns = [
    path('people/', views.employees_info, name='people'),
    path('person/<int:person_id>/', views.get_people_info, name='person_detail')
]