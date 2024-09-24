from django.forms import ModelForm

from doctor.models import Doctor


class StyleFormsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class DoctorForm(StyleFormsMixin, ModelForm):
    class Meta:
        model = Doctor
        fields = (
            "full_name",
            "specialty",
        )
