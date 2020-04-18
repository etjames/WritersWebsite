from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
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

class WritingTypes(models.Model):
	submission = models.ForeignKey(Submission, on_delete=models.CASCADE)

	WRITING_TYPES = (
		('poetry', 'Poetry'),
		('scripts', 'Scripts'),
		('longform', 'Long Form'),
	)
	writing_type = models.CharField(max_length=10, choices=WRITING_TYPES)


class Genres(models.Model):
	submission = models.ForeignKey(Submission, on_delete=models.CASCADE)

	GENRES = (
		('horror', 'Horror'),
		('romance', 'Romance'),
		('comedy', 'Comedy'),
		('action', 'Action'),
		('legal', 'Legal'),
	)
	genres = models.CharField(max_length=10, choices=GENRES)


class Themes(models.Model):
	submission = models.ForeignKey(Submission, on_delete=models.CASCADE)

	THEMES = (
		('lgbtq', "LGBTQ+"),
		('color', "Being a person of color"),
		('family', "Family"),
	)
	themes = models.CharField(max_length=10, choices=THEMES)
