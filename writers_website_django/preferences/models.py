from django.db import models
from django.forms import ModelForm

from django.contrib.auth.models import User

# Create your models here.
from submissions.models import Genre, WritingType, Theme, Submission

# Create your models here.
class Preference(models.Model):	
	# user = models.ForeignKey(User, on_delete=models.deletion.CASCADE)

	REVIEW_LENGTHS = (
		('5-10', "5-10 minutes"),
		('10-30', "10-30 minutes"),
		('30-60', "30-60 minutes"),
		('60+', "60 minutes +"),
	)
	review_time = models.CharField(max_length=10, choices=REVIEW_LENGTHS)

	genres = models.ManyToManyField(Genre, blank=True)
	writing_types = models.ManyToManyField(WritingType, blank=True)
	themes = models.ManyToManyField(Theme, blank=True)

class PreferenceForm(ModelForm):
	class Meta:
		model = Preference
		fields = '__all__'