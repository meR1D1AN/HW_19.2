from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField
from blog.models import Blog


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class BlogForm(StyleMixin, ModelForm):
    class Meta:
        model = Blog
        exclude = ('slug', 'created_at', 'views_count',)

    def clean_name_description(self):
        name = self.cleaned_data['name']
        description = self.cleaned_data['description']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        if any(word in name for word in forbidden_words):
            raise ValidationError('Нельзя добавлять запрешенные слова в название')
        if any(word in description for word in forbidden_words):
            raise ValidationError('Нельзя добавлять запрешенные слова в описание')
