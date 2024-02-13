from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    tags = Tag.objects.all()
    category = Category.objects.all()
    news = News.objects.filter(status=True).all()
    selected = News.objects.filter(selected=True).all()
    return render(request, 'index.html', context={
        'tags': tags,
        'category': category,
        'news': news,
        'selected': selected
    })


def news(request, pk):
    news = News.objects.get(id=pk)
    tags = Tag.objects.all()
    category = Category.objects.all()
    selected = News.objects.filter(selected=True).all()
    return render(request, 'news.html', context={
        'tags': tags,
        'category': category,
        'news': news,
        'selected': selected
    })

def categories(request, cat):
    tags = Tag.objects.all()
    category = Category.objects.all()
    news = News.objects.filter(status=True, category__url=cat).all()
    selected = News.objects.filter(selected=True).all()
    return render(request, 'index.html', context={
        'tags': tags,
        'category': category,
        'news': news,
        'selected': selected
    })