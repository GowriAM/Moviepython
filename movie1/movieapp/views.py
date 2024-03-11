from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Movie
from . forms import MovieForm
from django.db.models import Q


# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }

    return  render(request,'index.html',context)
def add_movie(request):

    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        # actors = request.POST.get('actors', )
        # category = request.POST.get('category', )
        # link = request.POST.get('link', )
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
        return redirect('/')
    return render(request, 'add_movie.html')
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return  render(request,"detail.html",{'movie':movie})


def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return  redirect('/')
    return  render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return  redirect('/')
    return render(request,'delete.html')

def movie_search(request):
    query = request.GET.get('q')
    if not query:
        return render(request, 'search.html', {'message': 'Please enter a search term.'})
    else:
        movies = Movie.objects.all().filter(Q(name__contains=query) |  Q(desc__contains=query))
        return render(request,'search.html',{'query':query,'movies': movies})

