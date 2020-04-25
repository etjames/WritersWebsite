from django.shortcuts import get_object_or_404, render, redirect

from .models import Submission, SubmissionForm
from reviews.models import Review

from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def prompts(request):
    return render(request, 'pages/prompts.html')

def anonymousfeedback(request):
    return render(request, 'pages/anonymousfeedback.html')

def rules(request):
    return render(request, 'pages/rules.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
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
    if request.user.is_authenticated == False:
        return redirect('/login')
    else:
        auth.logout(request)
        return render(request,'pages/logout.html')

# Create your views here.
def index(request):
    if request.user.is_authenticated == False:
        return redirect('/login')
    else:
        current_submission_list = Submission.objects.filter(author=request.user).order_by('title')
        context = {
            'current_submission_list': current_submission_list,
        }
        return render(request, 'submissions/index.html', context)

def detail(request, submission_id):
    if request.user.is_authenticated == False:
        return redirect('/login')
    else:
        submission = get_object_or_404(Submission, pk=submission_id)
        reviews = Review.objects.filter(submission=submission)
        context = {
            'submission': submission,
            'reviews': reviews
        }
        return render(request, 'submissions/detail.html', context)

def edit(request, submission_id):
    if request.user.is_authenticated == False:
        return redirect('/login')    
    else:
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
    if request.user.is_authenticated == False:
        return redirect('/login')
    if request.method == 'GET':
        context = {
            'form': SubmissionForm()
        }

        return render(request, 'submissions/new.html', context)

    elif request.method == 'POST':
        form_data = request.POST.copy()
        form_data['author'] = request.user
        submission_form = SubmissionForm(form_data)
        submission = submission_form.save(commit=False)
        submission.author = request.user
        submission.save()

        context = {
            'submission': submission,
        }

        return render(request, 'submissions/detail.html', context)
