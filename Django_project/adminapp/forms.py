from django.contrib.auth.forms import UserCreationForm, UserChangeForm
import django.forms as forms

from authapp.models import ShopClient
from mainapp.models import ProductCategory, Product


class FormControlMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""


class AdminShopUserRegisterForm(FormControlMixin, UserCreationForm):
    class Meta:
        model = ShopClient
        fields = (
            "username",
            "first_name",
            "last_name",
            "is_superuser",
            "is_staff",
            "password1",
            "password2",
            "email",
            "age",
            "avatar",
        )

    def clean_age(self):
        years_old = self.cleaned_data["age"]
        if years_old < 14:
            raise forms.ValidationError("Увы вам меньше 14 лет.")
        return years_old


class AdminShopUserUpdateForm(UserChangeForm):
    class Meta:
        model = ShopClient
        fields = (
            "username",
            "first_name",
            "last_name",
            "is_superuser",
            "is_staff",
            "is_active",
            "password",
            "email",
            "age",
            "avatar",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""
            if field_name == "password":
                field.widget = forms.HiddenInput()

    def clean_age(self):
        years_old = self.cleaned_data["age"]
        if years_old < 14:
            raise forms.ValidationError("Увы вам меньше 14 лет.")
        return years_old


class AdminProductCategoryCreateForm(FormControlMixin, forms.ModelForm):
    discount = forms.FloatField(
        label="скидка", required=False, min_value=0, max_value=90, initial=0
    )

    class Meta:
        model = ProductCategory
        fields = "__all__"


class AdminProductUpdateForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
