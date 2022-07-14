from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError

# форма связанная с моделями
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content', 'is_published', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

# кастомный валидатор на заполненность заголовка

    def clean_title(self):
        title = self.cleaned_data['title'] # получаем очищенные данные поля title из словаря
        if re.match('\d', title):  # проверяем, не начинается ли название с цифры
            raise ValidationError('Название не должно начинаться с цифры')
        return title

# валидатор для "Опубликовано", если галочка не стоит то не пропускает

    def clean_is_publised(self):
        is_published = self.cleaned_data['is_published']
        if re.match('\W', is_published):
            raise ValidationError('Отметьте галочку')
        return is_published

# валидатор для формы контента

    def clean_content(self):
        content = self.cleaned_data['content']
        if re.match('\w', content):
            raise ValidationError('Поле не должно быть пустым')
        return content