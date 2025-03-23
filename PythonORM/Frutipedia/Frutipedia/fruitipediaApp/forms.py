from django import forms

from Frutipedia.fruitipediaApp.models import Category, Fruit


class CategoryBaseForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Category name'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ""


class CategoryAddForm(CategoryBaseForm):
    pass


class BaseFruitForm(forms.ModelForm):

    class Meta:
        model = Fruit
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit name'}),
            'description': forms.TextInput(attrs={'placeholder': 'Enter fruit description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Enter fruit image URL'}),
            'nutrition': forms.NumberInput(attrs={'placeholder': 'Enter fruit nutrition'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ""


class AddFruitForm(BaseFruitForm):
    pass


class EditFruitForm(BaseFruitForm):
    pass


class DeleteFruitForm(BaseFruitForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True