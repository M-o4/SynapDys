from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_dys_user = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    difficulty_level = models.IntegerField()  # Niveau de difficulté de la leçon

    def __str__(self):
        return self.title

class Progress(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    date_completed = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.lesson}"
