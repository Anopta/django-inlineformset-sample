from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('add/', views.add_post, name='add_post'),
    path('update/<int:pk>/', views.update_post, name='update_post')
]
