from django.urls import path
from . import views
urlpatterns = [
    path("",views.media_list, name='media_list'),
    path("media/<int:pk>/",views.media_detail, name='media_detail'),
]
