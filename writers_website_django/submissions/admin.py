from django.contrib import admin

# Register your models here.
from .models import Submission, WritingTypes
admin.site.register(Submission)
admin.site.register(WritingTypes)