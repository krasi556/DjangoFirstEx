from django.urls import path

from categories import views

app_name = 'categories'

urlpatterns = [
    path('category/', views.list_of_categories, name='categories'),
    path('<int:category_id>/', views.current_category_detail, name='category_detail')
]
