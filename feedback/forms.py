from django.forms import ModelForm

from feedback.models import Feedback


class StyleFormsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class FeedbackForm(StyleFormsMixin, ModelForm):
    class Meta:
        model = Feedback
        fields = (
            "name",
            "phone",
            "email",
            "message",
        )
