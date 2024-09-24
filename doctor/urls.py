from django.urls import path
from doctor.apps import DoctorConfig
from doctor.views import (
    DoctorListView,
    DoctorCreateView,
    DoctorUpdateView,
    DoctorDetailView,
    DoctorDeleteView,
)

app_name = DoctorConfig.name

urlpatterns = [
    path("", DoctorListView.as_view(), name="doctor_list"),
    path("create/", DoctorCreateView.as_view(), name="doctor_create"),
    path("update/<int:pk>/", DoctorUpdateView.as_view(), name="doctor_update"),
    path("detail/<int:pk>/", DoctorDetailView.as_view(), name="doctor_detail"),
    path("delete/<int:pk>/", DoctorDeleteView.as_view(), name="doctor_delete"),
]
