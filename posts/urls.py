from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('like/<int:post_id>/', views.like, name='like'),
]
