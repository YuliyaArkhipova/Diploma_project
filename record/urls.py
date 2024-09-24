from django.urls import path
from record.apps import RecordConfig

from record.views import (
    RecordListView,
    RecordCreateView,
    RecordUpdateView,
    RecordDetailView,
    RecordDeleteView, ResultListView, ResultCreateView, ResultUpdateView, ResultDetailView, ResultDeleteView,
    AccountView,
)

app_name = RecordConfig.name

urlpatterns = [
    path("", RecordListView.as_view(), name="record_list"),
    path("create/", RecordCreateView.as_view(), name="record_create"),
    path("update/<int:pk>/", RecordUpdateView.as_view(), name="record_update"),
    path("detail/<int:pk>/", RecordDetailView.as_view(), name="record_detail"),
    path("delete/<int:pk>/", RecordDeleteView.as_view(), name="record_delete"),

    path("result/", ResultListView.as_view(), name="result_list"),
    path("result/create/", ResultCreateView.as_view(), name="result_create"),
    path("result/update/<int:pk>/", ResultUpdateView.as_view(), name="result_update"),
    path("result/detail/<int:pk>/", ResultDetailView.as_view(), name="result_detail"),
    path("result/delete/<int:pk>/", ResultDeleteView.as_view(), name="result_delete"),

    path("account/", AccountView.as_view(), name="account"),
]
