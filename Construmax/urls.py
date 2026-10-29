from django.urls import path
from Construmax.views import (
    CourseListView,
    CourseDetailView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
)

app_name = "construmax"

urlpatterns = [
    path("listar/", CourseListView.as_view(), name="course_list"),
    path("criar/", CourseCreateView.as_view(), name="course_create"),
    path("<int:pk>/ver/", CourseDetailView.as_view(), name="course_detail"),
    path("<int:pk>/editar/", CourseUpdateView.as_view(), name="course_update"),
    path("<int:pk>/deletar/", CourseDeleteView.as_view(), name="course_delete"),
]