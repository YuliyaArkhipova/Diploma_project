from django.forms import ModelForm

from services.models import Services


class StyleFormsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class ServicesForm(StyleFormsMixin, ModelForm):
    class Meta:
        model = Services
        fields = (
            "services_name",
            "category",
            "price",
        )
