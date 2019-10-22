from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    # /music/ex. 123/
    path('<int:album_id>/', views.details, name='details'),

    # /music/ex. 123/
    path('<int:album_id>/favourite', views.favourite, name='favourite'),
]
