from django.urls import path
from . import views
urlpatterns = [
    path("",views.media_list, name='media_list'),
    path("media/<int:pk>/",views.media_detail, name='media_detail'),
    path('media/<int:pk>/delete/', views.media_delete, name='media_delete'),
    path('media/<int:pk>/download/', views.media_download, name='media_download'),
]
