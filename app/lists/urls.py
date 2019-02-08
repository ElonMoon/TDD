from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.home_page, name='home'),
    path(r'lists/the-only-list-in-the-world/', views.view_list, name='view-list'),
]
