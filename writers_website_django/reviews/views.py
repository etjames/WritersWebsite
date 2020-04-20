from django.shortcuts import get_object_or_404, render, redirect

from .models import Review, ReviewForm
from submissions.models import Submission
from preferences.models import Preference

# Create your views here.
def list(request):
    if request.user.is_authenticated == False:
        return redirect('/login')
    reviews = Review.objects.filter(reviewer=request.user)
    context = {
        'reviews': reviews
    }
    return render(request, 'reviews/list.html', context)

def matches(request):
    # Fetch user preferences
    if request.user.is_authenticated == False:
        return redirect('/login')
    preferences = Preference.objects.filter(user=request.user).first()

    submissions = Submission.objects.exclude(author=request.user)
    submissions = submissions.filter(review_time=preferences.review_time)     

    context = {
        'submissions': submissions
    }
    
    return render(request, 'reviews/matches.html', context)

def new(request, submission_id):
    if request.user.is_authenticated == False:
        return redirect('/login')
    submission = Submission.objects.get(pk=submission_id)
    review = Review.objects.filter(submission=submission).filter(reviewer=request.user).first()
    if review is None:
        review = Review(submission=submission, reviewer=request.user)
        review.save()

    return redirect(f'/reviews/edit/{review.id}')

def edit(request, review_id):
    if request.user.is_authenticated == False:
        return redirect('/login')
    review = Review.objects.get(pk=review_id)
    if request.method == 'GET':
        context = {
            'review': review,
            'form': ReviewForm(instance=review)
        }
        return render(request, 'reviews/edit.html', context)

    elif request.method == 'POST':
        form_data = request.POST.copy()
        form_data['reviewer'] = request.user
        review_form = ReviewForm(form_data, instance=review)
        review = review_form.save()

        context = {
            'review': review,
        }

        return redirect('/reviews/')
