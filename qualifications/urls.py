from django.urls import path

from qualifications import views

app_name = 'qualifications'
urlpatterns = [
    path('', views.show_qualifications, name='qualifications'),
    path('qualifications-<int:person_id>/', views.show_person_qualification, name='qualification')

]
