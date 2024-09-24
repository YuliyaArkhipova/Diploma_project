from django.conf import settings
from django.views.generic import TemplateView
from django.http import Http404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.core.cache import cache

from rest_framework.reverse import reverse_lazy

from doctor.models import Doctor
from feedback.forms import FeedbackForm
from feedback.models import Feedback
from services.forms import ServicesForm
from services.models import Services, Category


class HomeView(TemplateView):
    template_name = "services/home.html"

    def get(self, request, *args, **kwargs):
        form = FeedbackForm()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            Feedback.objects.create(name=name, email=email, message=message)
            return self.render_to_response({"success": True})
        else:
            return self.render_to_response({"success": False, "errors": form.errors})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ContactView(TemplateView):
    template_name = "services/contact.html"

    def get(self, request, *args, **kwargs):
        form = FeedbackForm()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            Feedback.objects.create(name=name, email=email, message=message)
            return self.render_to_response({"success": True})
        else:
            return self.render_to_response({"success": False, "errors": form.errors})


class CompanyView(TemplateView):
    template_name = "services/company.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["doctors"] = Doctor.objects.all()
        return context_data


class CategoryListView(ListView):
    model = Category
    template_name = "services/category_list.html"
    context_object_name = "object_list"


class CategoryDetailView(ListView):
    model = Category
    template_name = "services/category_detail.html"
    context_object_name = "services_list"

    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        return Services.objects.filter(category_id=category_id)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('pk')
        context_data["category"] = Category.objects.get(pk=category_id)
        return context_data


class ServicesListView(ListView):
    model = Services
    template_name = "services/services_list.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "Список услуг"
        context_data["categories"] = Category.objects.all()
        return context_data


class ServicesDetailView(DetailView):
    model = Services
    template_name = "services/services_detail.html"


class ServicesCreateView(CreateView):
    model = Services
    form_class = ServicesForm
    success_url = reverse_lazy("services/services_list")

    def form_valid(self, form):
        new_client = form.save()
        if new_client.user is None:
            new_client.user = self.request.user
        return super().form_valid(form)


class ServicesUpdateView(UpdateView):
    model = Services
    form_class = ServicesForm
    success_url = reverse_lazy("services/services_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class ServicesDeleteView(DeleteView):
    model = Services
    success_url = reverse_lazy("services/services_list")
