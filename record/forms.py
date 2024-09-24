from django.forms import ModelForm

from record.models import Record, Result


class StyleFormsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class RecordForm(StyleFormsMixin, ModelForm):
    class Meta:
        model = Record
        fields = (
            "category",
            "services",
            "doctor",
            "patient",
            "date",
            "time",

        )


class ResultForm(StyleFormsMixin, ModelForm):
    class Meta:
        model = Result
        fields = (
            "record",
            "patient",
            "title",
            "appointments",
            "file",
        )

