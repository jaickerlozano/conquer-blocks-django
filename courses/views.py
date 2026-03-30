from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Course


class CursosListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'courses/courses_list.html'
    context_object_name = 'courses'
    paginate_by = 10
    ordering = ['-created_at']


class CursosDetailView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'courses/courses_detail.html'
    context_object_name = 'course'

    def get_queryset(self):
        return Course.objects.filter(pk=self.kwargs['id'])
