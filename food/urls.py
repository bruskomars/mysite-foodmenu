from django.urls import path
from . import views

urlpatterns=[
    path("", views.home, name="home"),
    path("item/", views.item, name='item'),
    path("<int:pk>/", views.detail, name='detail'),

    # add items
    path('add', views.create_item, name='create_item'),

    # edit items
    path('update/<int:pk>', views.update_item, name='update_item'),

    # delete items
    path('delete/<int:pk>', views.delete_item, name='delete_item'),
]