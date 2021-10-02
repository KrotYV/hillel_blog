from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, TemplateView

from .forms import RegisterForm
from .models import Post

User = get_user_model()


class RegisterFormView(generic.FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.save()

        username = self.request.POST['username']
        password = self.request.POST['password1']

        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(RegisterFormView, self).form_valid(form)


class UserProfile(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "registration/profile.html"

    def get_object(self, queryset=None):
        user = self.request.user
        return user


class HomePageView(TemplateView):
    template_name = 'index.html'


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'brief_description', 'full_description']
    template_name = 'create_post.html'
    success_url = reverse_lazy('')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        self.object = post
        return HttpResponseRedirect(self.get_success_url())
