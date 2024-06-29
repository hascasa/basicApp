from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_insurance, name='add_insurance'),
    path('list/', views.insurance_list, name='insurance_list'),
    path('update/<int:pk>/', views.update_insurance, name='update_insurance'),
    path('delete/<int:pk>/', views.delete_insurance, name='delete_insurance'),
    path('filter-list/', views.insurance_list_view, name='filter_list'),
]

