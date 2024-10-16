from django.urls import path

from . import views
from .views import PackageCreateView  # get_projects_by_client,
from .views import (
    PackageDetailView,
    PackageListView,
    create_client,
    create_project,
    get_projects,
)

app_name = "shots"

urlpatterns = [
    path("", PackageListView.as_view(), name="main"),
    path(
        "package/create/", PackageCreateView.as_view(), name="create_package"
    ),  # Thêm đường dẫn này
    path("package/<slug>/", PackageDetailView.as_view(), name="detail_package"),
    path(
        "<str:selected_year>/<str:selected_month>/",
        PackageListView.as_view(),
        name="main_year_month",
    ),
    path("projects/", get_projects, name="get_projects_by_client"),
    path("create-client/", create_client, name="create_client"),
    path("create-project/", create_project, name="create_project"),
]
