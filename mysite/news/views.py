from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News, Category
from django.http import Http404
from .forms import NewsForm

# Create your views here.
def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, template_name='news/index.html', context=context)

def get_category(request, category_id):
    try:
        news = News.objects.filter(category_id=category_id)
        category = Category.objects.get(pk=category_id)
    except News.DoesNotExist:
        raise Http404("Здесь не на что смотреть")
    return render(request, 'news/category.html', {'news': news, 'category': category})



def view_news(request, news_id):
    try:
        news_item = News.objects.get(pk=news_id)
    except News.DoesNotExist:
        raise Http404("Нет новостей на этой странице. Нечего глазеть.")
    return render(request, 'news/view_news.html', {"news_item": news_item})


def add_news(request):
    try:
        if request.method == 'POST':
            form = NewsForm(request.POST)
            if form.is_valid():
                news = News.objects.create(**form.cleaned_data)
                return redirect(news)
        else:
            form = NewsForm()
    except News.DoesNotExist:
        raise Http404("Не вышло, такой страницы не существует")
    return render(request, 'news/add_news.html', {'form': form})