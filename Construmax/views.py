from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,DeleteView
from courses.forms import Construmax  # troque courses pelo nome do seu app
from courses.models import Construmax

class CourseListView(ListView):
    model = Course
    template_name = "courses/course_list.html"
    context_object_name = "courses"
    paginate_by = 10

class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"
    context_object_name = "course"

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/course_form_create.html"
    success_url = reverse_lazy("courses:course_list")

class CourseUpdateView(UpdateView):
    model = Construmax
    form_class = CourseForm
    # troque courses pelo nome do seu app
    template_name = "courses/course_form_update.html"
    context_object_name = "course"
    success_url = reverse_lazy("courses:course_list")

class CourseDeleteView(DeleteView):
    model = Construmax
    # troque courses pelo nome do seu app
    template_name = "courses/course_confirm_delete.html"
    context_object_name = "course"
    success_url = reverse_lazy("courses:course_list")