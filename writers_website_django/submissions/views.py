from django.shortcuts import get_object_or_404, render

from .models import Submission

# Create your views here.
def index(request):
	current_submission_list = Submission.objects.order_by('title')
	context = {
		'current_submission_list': current_submission_list,
	}
	return render(request, 'index.html', context)

def detail(request, submission_id):
	submission = get_object_or_404(Submission, pk=submission_id)
	context = {
		'submission': submission
	}
	return render(request, 'detail.html', context)
