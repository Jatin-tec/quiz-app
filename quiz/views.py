from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse
from quiz.models import Question, QuizSession
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from random import choice

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('quiz-start')
        return render(request, 'authentication/login.html', {'error': 'Invalid credentials'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('quiz-login')


@method_decorator(login_required, name='dispatch')
class StartQuizView(View):
    def get(self, request):
        session = QuizSession.objects.create(user=request.user)
        request.session['quiz_id'] = session.id
        return redirect('quiz-question')


@method_decorator(login_required, name='dispatch')
class QuestionView(View):
    def get(self, request):
        session_id = request.session.get('quiz_id')
        if not session_id:
            return redirect('quiz-start')

        session = QuizSession.objects.get(id=session_id)
        visited_questions = session.visited_questions.all()
        remaining_questions = Question.objects.exclude(id__in=visited_questions)


        if not remaining_questions.exists():
            return redirect('quiz-results')

        question = choice(remaining_questions)
        return render(request, 'quiz/question.html', {'question': question})

    def post(self, request):
        session_id = request.session.get('quiz_id')
        if not session_id:
            return JsonResponse({'error': 'No active quiz session.'}, status=400)

        session = QuizSession.objects.get(id=session_id)
        question_id = request.POST.get('question_id')
        action = request.POST.get('action')

        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            return JsonResponse({'error': 'Invalid question.'}, status=400)

        if action == 'submit':
            selected_option = request.POST.get('selected_option')
            session.total_questions += 1
            if question.correct_option == selected_option:
                session.correct_answers += 1
            else:
                session.incorrect_answers += 1

            session.visited_questions.add(question)
        elif action == 'skip':
            session.visited_questions.add(question)
            session.skipped_questions.add(question)

        session.save()
        return redirect('quiz-question')


@method_decorator(login_required, name='dispatch')
class ResultsView(View):
    def get(self, request):
        session_id = request.session.get('quiz_id')
        if not session_id:
            return redirect('quiz-start')

        session = QuizSession.objects.get(id=session_id)
        all_questions = Question.objects.all()
        unanswered_questions = session.skipped_questions.all()

        return render(request, 'quiz/results.html', {
            'session': session,
            'unanswered_questions': unanswered_questions,
        })
