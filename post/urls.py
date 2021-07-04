from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('new_post/',views.new_post,name='new_post'),
    path('post_list/',views.post_list,name='post_list'),
    path('post_detail/<int:post_id>/',views.post_detail,name='post_detail'),
]
