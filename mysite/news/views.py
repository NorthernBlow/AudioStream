from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News, Category
from django.http import Http404
from .forms import NewsForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

class HomeNews(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'  # переопределение имени с object_list на news
    extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        # получаем новости только отмеченные к публикации
        return News.objects.filter(is_published=True)

class NewsByCategory(ListView):
    model = News
    template_name = 'news/list_category.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsByCategory, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        # получаем новости только отмеченные к публикации
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    #pk_url_kwarg = 'news_id'
    #template_name = 'news/view_news'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
# так же здесь джанго ожидает метод get_absolute_url из модели
# но можно переопределить здесь функцию редиректа
    success_url = reverse_lazy('home')


#def index(request):
#    news = News.objects.all()
#    context = {
#        'news': news,
#        'title': 'Список новостей',
#    }
#    return render(request, template_name='news/index.html', context=context)

#def get_category(request, category_id):
#    try:
#        news = News.objects.filter(category_id=category_id)
#        category = Category.objects.get(pk=category_id)
#    except News.DoesNotExist:
#        raise Http404("Здесь не на что смотреть")
#    return render(request, 'news/category.html', {'news': news, 'category': category})


def view_news(request, news_id):
    try:
        news_item = News.objects.get(pk=news_id)
    except News.DoesNotExist:
        raise Http404("Нет новостей на этой странице. Нечего глазеть.")
    return render(request, 'news/view_news.html', {"news_item": news_item})


#def add_news(request):
#    try:
#        if request.method == 'POST':
#            form = NewsForm(request.POST)
#            if form.is_valid():
#                #print(form.cleanded_data)
#                #news = News.objects.create(**form.cleaned_data) # форма не связанная с моделями
#                news = form.save() #форма связанная с моделями
#                return redirect(news)
#        else: #если данные пришли методом GET то создаем пустую форму
#            form = NewsForm()
#    except News.DoesNotExist:
#        raise Http404("Не вышло, такой страницы не существует")
#    return render(request, 'news/add_news.html', {'form': form})