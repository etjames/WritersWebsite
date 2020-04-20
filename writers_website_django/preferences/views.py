from django.shortcuts import get_object_or_404, render, redirect

from .models import Preference, PreferenceForm

# Create your views here.
def edit(request):
    if request.user.is_authenticated == False:
        return redirect('/login')
    preferences = Preference.objects.filter(user=request.user).first()
    if preferences is None:
        preferences = Preference()
    preferences.user = request.user
    if request.method == 'GET':
        context = {
            'preferences': preferences,
            'form': PreferenceForm(instance=preferences),
        }
        return render(request, 'preferences/edit.html', context)

    elif request.method == 'POST':
        form_data = request.POST.copy()
        form_data['user'] = request.user
        #form_data['user_id'] = request.user.id
        preference_form = PreferenceForm(form_data, instance=preferences)
        preferences = preference_form.save()

        context = {
            'preferences': preferences,
            'form': PreferenceForm(instance=preferences),
            'saved': True,
        }

        return render(request, 'preferences/edit.html', context)
