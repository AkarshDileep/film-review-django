from django.shortcuts import render
from . models import movie
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required(login_url='login')
def movieadd(request):
    movielist=movie.objects.all()
    content={'moviee':movielist}
    return render(request,'home.html',content)

@login_required(login_url='login')
def list_movies(request):
    
    movielist = movie.objects.all()
    
    content={'moviee':movielist}
    return render(request,'movie_list.html',content)


@login_required(login_url='login')
def list_movies1(request):
    
    movielist = movie.objects.all()
    
    content={'moviee':movielist}
    return render(request,'movie_list1.html',content)
 
@login_required(login_url='login')
def list_movies2(request):
    
    movielist = movie.objects.all()
    
    content={'moviee':movielist}
    return render(request,'movie_list2.html',content)




   