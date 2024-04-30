from django.urls import path
from . import views 

urlpatterns = [
    path('', views.get_user),
    path('user/<str:username>/', views.get_user),
    path('repos/<str:username>/', views.get_repos),
    path('save_user/', views.save_user),
    path('delete_user/', views.delete_user),
    path('save_repos/', views.save_repos),
    path('delete_repos/<str:username>/', views.delete_repos, name='delete_repos'),
   
    # Other URL patterns for your application...
]