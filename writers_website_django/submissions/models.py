from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name

class WritingType(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name	

class Theme(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name

class Submission(models.Model):
	# info about the submission
	author_name = models.CharField(max_length=128)
	title = models.CharField(max_length=128)
	content = models.TextField()

	REVIEW_LENGTHS = (
		('5-10', "5-10 minutes"),
		('10-30', "10-30 minutes"),
		('30-60', "30-60 minutes"),
		('60+', "60 minutes +"),
	)
	review_time = models.CharField(max_length=10, choices=REVIEW_LENGTHS)

	min_review_count = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
	max_review_count = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

	message_to_reader = models.TextField()

	genres = models.ManyToManyField(Genre, blank=True)
	writing_types = models.ManyToManyField(WritingType, blank=True)
	themes = models.ManyToManyField(Theme, blank=True)

	author = models.ForeignKey(User, on_delete=models.CASCADE)


class SubmissionForm(ModelForm):
	class Meta:
		model = Submission
		# fields = ['author', 'title', 'content', 'review_time', 'message_to_reader']
		fields = '__all__'
		exclude = ['author']