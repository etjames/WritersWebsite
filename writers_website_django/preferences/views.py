from django.shortcuts import get_object_or_404, render

from .models import Preference, PreferenceForm

# Create your views here.
def edit(request):
    preferences = Preferences.get.filter(user=request.user)
    preferences = Preference.get(id=1)
    context = {
        "preferences": preferences
    }
    return render(request, 'user_preferences/edit.html')