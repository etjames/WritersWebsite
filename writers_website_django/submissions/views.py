from django.shortcuts import get_object_or_404, render

from .models import Submission, SubmissionForm

# Create your views here.
def index(request):
    current_submission_list = Submission.objects.order_by('title')
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
