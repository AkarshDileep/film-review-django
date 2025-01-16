from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from . models import review
from movies.models import movie
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def moviedetail(request,pk):
    
    movielist=movie.objects.get(pk=pk)
    
    reviewlist=review.objects.all()
    content={'moviee':movielist,
              'reviewss':reviewlist}

    
    if request.POST:
        name=pk
        email=request.POST.get('email')
        reviews=request.POST.get('reviews')
        c1=review(name=name,mail=email,reviews=reviews)
        c1.save()
    return render(request,'movie.html',content)
    

def list_movies(request,):
    return render(request,'movie_list.html')

    