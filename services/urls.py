from django.urls import path

from services.views import (
    ServicesListView,
    ServicesCreateView,
    ServicesUpdateView,
    ServicesDetailView,
    ServicesDeleteView,
    HomeView,
    CategoryListView,
    ContactView, CompanyView, CategoryDetailView,
)
from services.apps import ServicesConfig

app_name = ServicesConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("company/", CompanyView.as_view(), name="company"),
    path("category/", CategoryListView.as_view(), name="category_list"),
    path("category/detail/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),
    path("services/", ServicesListView.as_view(), name="services_list"),
    path("services/create/", ServicesCreateView.as_view(), name="services_create"),
    path("services/detail/<int:pk>/", ServicesDetailView.as_view(), name="services_detail"),
    path("services/delete/<int:pk>/", ServicesDeleteView.as_view(), name="services_delete"),
]
