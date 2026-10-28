from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from courses.views import CourseListView, CourseCreateView,CourseDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from courses.views import ConstrumaxListView  # troque courses pelo nome do seu app

app_name = "Construmax"

urlpatterns = [
    path("listar/", CourseListView.as_view(), name="course_list"),
]



app_name = "courses"

urlpatterns = [
    path("listar/", CourseListView.as_view(), name="course_list"),
    path("<int:pk>/ver/", CourseDetailView.as_view(), name="course_detail"),
]

from courses.views import CourseListView, CourseCreateView, CourseUpdateView

app_name = "courses"

urlpatterns = [
    path("listar/", CourseListView.as_view(), name="course_list"),
    path("criar/", CourseCreateView.as_view(), name="course_create"),
    path("<int:pk>/editar/", CourseUpdateView.as_view(), name="course_update"),
]

app_name = "courses"

urlpatterns = [
    path("listar/", CourseListView.as_view(), name="course_list"),
    path("criar/", CourseCreateView.as_view(), name="course_create"),
    path("<int:pk>/editar/", CourseUpdateView.as_view(), name="course_update"),
    path("<int:pk>/deletar/", CourseDeleteView.as_view(), name="course_delete"),