from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"Tag: {self.name}"

    def get_absolute_url(self):
        return reverse("tad-list")


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks", blank=True)

    def __str__(self):
        return f"Task: {self.content[:50]}"

    def get_absolute_url(self):
        return reverse("home")

    def toggle_status(self):
        self.is_done = not self.is_done
        self.save()

    class Meta:
        ordering = ["is_done", "-created_at"]
