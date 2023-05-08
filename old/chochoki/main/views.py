import base64
import os

from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User as DUser
from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render as r2, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .models import *


def render(request, template_name, context2=None, content_type=None, status=None, using=None):
    context = context2 if context2 is not None else {}
    if 'page' not in context:
        context['page'] = ''
    return r2(request, template_name, context, content_type, status, using)


class Views(WSGIRequest):
    if 'pychram':
        user: DUser = DUser()

    def index(self):
        return render(self, 'main/index.html', {'page': 'index'})

    def about(self):
        return render(self, 'main/about.html', {'page': 'about'})

    def games(self):
        games = Game.objects.all()
        return render(self, 'main/games.html', {'games': games, 'page': 'games'})

    def game(self, game):
        try:
            game = Game.objects.get(name=game)
        except Game.DoesNotExist:
            raise Http404
        if not game.is_published and not self.user.is_superuser:
            raise Http404
        game.html = game.html.replace('{{game.name}}', game.name)
        return render(self, 'main/game.html', {"game": game})

    def regenerate_token(self, game, token):
        try:
            game = Game.objects.get(name=game)
        except Game.DoesNotExist:
            raise Http404
        if not self.user.is_superuser or not token == game.token:
            raise Http404
        game.token = base64.b64encode(os.urandom(20)).decode().replace('=', '').replace('/', '').replace('\\', '')
        game.save()
        return redirect(f'/admin/main/game/{game.pk}/change')

    def page_not_found(self, exception):
        return HttpResponseNotFound(f"<h1>404 not found</h1>")

    def logout_user(self):
        logout(self)
        return redirect('login')

    def profile(self):
        return render(self, 'main/index.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # c_def = self.get_user_context(title='register')
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        User.objects.create(username=user.username)
        login(self.request, user)
        return redirect('index')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('index')


views = Views
