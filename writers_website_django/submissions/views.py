from django.shortcuts import get_object_or_404, render, redirect

from .models import Submission, SubmissionForm

from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'pages/signup.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        return redirect('/submissions')
 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
 
        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('/submissions')
 
        else:
            messages.error(request, 'Error wrong username/password')
 
    return render(request, 'pages/login.html')
 
 
def logout(request):
    auth.logout(request)
    return render(request,'pages/logout.html')

# Create your views here.
def index(request):
    current_submission_list = Submission.objects.filter(author=request.user).order_by('title')
    context = {
        'current_submission_list': current_submission_list,
    }
    return render(request, 'submissions/index.html', context)

def detail(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    context = {
        'submission': submission,
    }
    return render(request, 'submissions/detail.html', context)

def edit(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    if request.method == 'GET':
        context = {
            'submission': submission,
            'form': SubmissionForm(instance=submission)
        }

        return render(request, 'submissions/edit.html', context)

    elif request.method == 'POST':
        submission_form = SubmissionForm(request.POST, instance=submission)
        submission_form.save()

        context = {
            'submission': submission,
        }

        return render(request, 'submissions/detail.html', context)


def new(request):
    if request.method == 'GET':
        context = {
            'form': SubmissionForm()
        }

        return render(request, 'submissions/new.html', context)

    elif request.method == 'POST':
        submission_form = SubmissionForm(request.POST)
        submission = submission_form.save()

        context = {
            'submission': submission,
        }

        return render(request, 'submissions/detail.html', context)
