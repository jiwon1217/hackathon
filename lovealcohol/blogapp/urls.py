from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('blogpost/', views.blogpost, name="blogpost"),
    path('update/<int:pk>',views.update, name="update"),#
    path('delete/<int:pk>',views.delete, name="delete"),
    path('',views.home, name="home"),
    path('myhome',views.myhome, name="myhome"),
    path('edit/<int:blog_id>',views.edit,name="edit"),


    
]