from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.ManagerAppView.as_view(), name='app'),
    path('add/', views.ManagerAppAddView.as_view(), name='app_add'),
    path('edit/<int:pk>/', views.ManagerAppEditView.as_view(), name='app_edit')
]
