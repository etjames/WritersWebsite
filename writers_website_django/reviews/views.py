from django.shortcuts import get_object_or_404, render

from .models import Review, ReviewForm

# Create your views here.
def edit(request):
    return render(request, 'reviews/edit.html')