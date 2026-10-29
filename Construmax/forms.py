from django import forms
from Construmax.models import Course # troque courses pelo nome do seu app


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            "name",
            "description",
            "workload",
            "period",
            "teacher",
            "material",
            "image",
        ]
        