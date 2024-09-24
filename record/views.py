from django.http import Http404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView, TemplateView,
)
from rest_framework.reverse import reverse_lazy

from record.forms import RecordForm, ResultForm
from record.models import Record, Result


class RecordListView(ListView):
    model = Record
    template_name = "record/record_list.html"


class RecordDetailView(DetailView):
    model = Record
    template_name = "record/record_detail.html"


class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm
    success_url = reverse_lazy("record/record_list")


class RecordUpdateView(UpdateView):
    model = Record
    form_class = RecordForm
    success_url = reverse_lazy("record/record_list")


class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy("record/record_list")


class ResultListView(ListView):
    model = Result
    template_name = "record/result_list.html"


class ResultDetailView(DetailView):
    model = Result
    template_name = "record/result_detail.html"


class ResultCreateView(CreateView):
    model = Result
    form_class = ResultForm
    success_url = reverse_lazy("record/result_list")


class ResultUpdateView(UpdateView):
    model = Result
    form_class = RecordForm
    success_url = reverse_lazy("record/result_list")


class ResultDeleteView(DeleteView):
    model = Result
    success_url = reverse_lazy("record/result_list")


class AccountView(TemplateView):
    template_name = "record/account.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        context['records'] = Record.objects.filter(patient=user.patient_name)
        context['results'] = Result.objects.filter(patient=user)
        return context
