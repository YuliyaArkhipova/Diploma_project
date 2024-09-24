from django.http import Http404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from rest_framework.reverse import reverse_lazy

from doctor.forms import DoctorForm
from doctor.models import Doctor


class DoctorListView(ListView):
    model = Doctor
    template_name = "doctor/doctor_list.html"


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = "doctor/doctor_detail.html"
    context_object_name = "doctor_list"


class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy("doctor/doctor_list")

    def form_valid(self, form):
        new_client = form.save()
        if new_client.user is None:
            new_client.user = self.request.user
        return super().form_valid(form)


class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy("doctor/doctor_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class DoctorDeleteView(DeleteView):
    model = Doctor
    success_url = reverse_lazy("doctor/doctor_list")
