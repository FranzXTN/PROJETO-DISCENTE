from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from Construmax.forms import CourseForm
from Construmax.models import Course


class CourseListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = reverse_lazy("accounts:login")
    permission_required = "Construmax.view_course"
    model = Course
    template_name = "construmax/course_list.html"
    context_object_name = "courses"
    paginate_by = 10


class CourseDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    login_url = reverse_lazy("accounts:login")
    permission_required = "Construmax.view_course"
    model = Course
    template_name = "construmax/course_detail.html"
    context_object_name = "course"


class CourseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy("accounts:login")
    permission_required = "Construmax.add_course"
    model = Course
    form_class = CourseForm
    template_name = "construmax/course_form_create.html"
    success_url = reverse_lazy("construmax:course_list")


class CourseUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy("accounts:login")
    permission_required = "Construmax.change_course"
    model = Course
    form_class = CourseForm
    template_name = "construmax/course_form_update.html"
    context_object_name = "course"
    success_url = reverse_lazy("construmax:course_list")


class CourseDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy("accounts:login")
    permission_required = "Construmax.delete_course"
    model = Course
    template_name = "construmax/course_confirm_delete.html"
    context_object_name = "course"
    success_url = reverse_lazy("construmax:course_list")