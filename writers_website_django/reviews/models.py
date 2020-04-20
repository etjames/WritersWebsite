from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.forms import ModelForm
from django.contrib.auth.models import User

from submissions.models import Submission

class Review(models.Model):
	response = models.TextField()
	reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
	submission = models.ForeignKey(Submission, on_delete=models.CASCADE)

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = '__all__'
		exclude = ['reviewer', 'submission']