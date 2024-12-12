from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    CORRECT_OPTION_CHOICES = [
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D'),
    ]
    question_text = models.CharField(max_length=255)
    
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    
    correct_option = models.CharField(max_length=1, choices=CORRECT_OPTION_CHOICES)

    def __str__(self):
        return self.question_text

class QuizSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    total_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)

    visited_questions = models.ManyToManyField(Question, related_name='visited_sessions', blank=True)
    skipped_questions = models.ManyToManyField(Question, related_name='skipped_sessions', blank=True)
