from django.urls import path
from . import views

urlpatterns=[
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profilepage, name='profile'),
]