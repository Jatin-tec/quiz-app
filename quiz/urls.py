from django.urls import path
from quiz.views import StartQuizView, QuestionView, ResultsView

urlpatterns = [
    path('', StartQuizView.as_view(), name='quiz-start'),
    path('question/', QuestionView.as_view(), name='quiz-question'),
    path('results/', ResultsView.as_view(), name='quiz-results'),
]