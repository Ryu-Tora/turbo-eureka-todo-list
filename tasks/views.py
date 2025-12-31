from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from django.shortcuts import render, redirect, get_object_or_404

from tasks.models import Task, Tag
from tasks.forms import TaskForm, TagForm


def home(request):
    tasks = Task.objects.all()
    return render(request, "todolist/home.html", {"tasks": tasks})


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todolist/task_form.html"
    success_url = reverse_lazy("home")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todolist/task_form.html"
    success_url = reverse_lazy("home")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todolist/task_confirm_delete.html"
    success_url = reverse_lazy("home")


class TaskToggleView(View):

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.toggle_status()
        return redirect("home")


class TagListView(ListView):
    model = Tag
    template_name = "todolist/tag_list.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todolist/tag_form.html"
    success_url = reverse_lazy("home")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todolist/tag_form.html"
    success_url = reverse_lazy("home")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "todolist/tag_confirm_delete.html"
    success_url = reverse_lazy("home")
