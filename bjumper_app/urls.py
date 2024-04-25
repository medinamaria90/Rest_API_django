from django.urls import path
from . import views 

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.getData),
    path('repos/', views.getReposData),
    path('post/', views.postData),
    # Other URL patterns for your application...
]