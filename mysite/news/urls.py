from django.urls import path
from .views import view_news, HomeNews, NewsByCategory, ViewNews, CreateNews

urlpatterns = [
    path('', HomeNews.as_view(extra_context={'title': 'Главная'}), name='home'),
    #path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    #path('news/add-news', add_news, name='add_news'),
    path('news/add-news', CreateNews.as_view(), name='add_news'),
]