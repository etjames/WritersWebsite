from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.forms import ModelForm

class Review(models.Model):
	title = "This is a Story"
	content = "Here is some story content for testing."
	message_from_author = "Here is a message the author left for you."
	response = models.TextField()

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = '__all__'