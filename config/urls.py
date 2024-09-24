from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("services.urls", namespace="services")),
    path("doctor/", include("doctor.urls", namespace="doctor")),
    path("feedback/", include("feedback.urls", namespace="feedback")),
    path("record/", include("record.urls", namespace="record")),
    path("users/", include("users.urls", namespace="user")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
