from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Question, Answer

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
