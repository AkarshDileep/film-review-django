from django.urls import path
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('home', views.movieadd,name='home'),
    path('movie_lists/malayalam',views.list_movies,name='movielist'),
    path('movie_lists/bollywood',views.list_movies1,name='movielist1'),
    path('movie_lists/hollywood',views.list_movies2,name='movielist2'),
    
   
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)