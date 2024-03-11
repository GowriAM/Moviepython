
from django.urls import path
from . import views
app_name='movieapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add_movie',views.add_movie,name='add_movie'),
    path('update/<int:id>/', views.update,name='update'),
    path('delete/<int:id>/', views.delete,name='delete'),
    path('search/', views.movie_search, name='movie_search'),
]