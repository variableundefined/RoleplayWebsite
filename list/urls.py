from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('classicspelllist', views.spell_list, name='spell_list'),
    path('tablespelllist', views.table_list, name='table_list'),
    path('list/<int:pk>/', views.spell_detail, name='spell_detail'),
]