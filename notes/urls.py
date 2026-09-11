from django.urls import path

from notes import views

urlpatterns = [
    path('notes/', views.notes_view, name='notes_view')
]

