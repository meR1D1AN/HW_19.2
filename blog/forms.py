from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField
from blog.models import Blog


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class BlogForm(StyleMixin, ModelForm):
    class Meta:
        model = Blog
        exclude = (
            "created_at",
            "views_count",
        )

    def clean_name(self):
        name = self.cleaned_data["name"].lower()
        forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        for word in forbidden_words:
            if word in name:
                raise ValidationError("Нельзя добавлять запрещенные слова в название")
        return name

    def clean_description(self):
        description = self.cleaned_data["description"].lower()
        forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        for word in forbidden_words:
            if word in description:
                raise ValidationError("Нельзя добавлять запрещенные слова в название")
        return description
