from django import forms
from .mixins import BootstrapFormMixin
from catalog.models import Product, Version


class ProductForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if any(banned_word in name.lower() for banned_word in banned_words):
            raise forms.ValidationError("Название продукта содержит запрещённые слова.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if any(banned_word in description.lower() for banned_word in banned_words):
            raise forms.ValidationError("Описание продукта содержит запрещённые слова.")
        return description

class VersionForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ['product', 'version_number', 'version_name', 'is_current']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_current'].widget.attrs.update({'class': 'form-check-input'})
