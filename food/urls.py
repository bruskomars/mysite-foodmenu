from django.urls import path
from . import views

urlpatterns=[
    path("", views.home, name="home"),
    # path("", views.IndexClassView.as_view(), name="home"), # CLASS BASE VIEW SAMPLE
    path("item/", views.item, name='item'),
    # path("<int:pk>/", views.detail, name='detail'),
    path("<int:pk>/", views.FoodDetail.as_view(), name='detail'), # CLASS BASE VIEW SAMPLE

    # add items
    # path('add', views.create_item, name='create_item'),
    path('add', views.CreateItem.as_view(), name='create_item'),

    # edit items
    path('update/<int:pk>', views.update_item, name='update_item'),

    # delete items
    path('delete/<int:pk>', views.delete_item, name='delete_item'),
]