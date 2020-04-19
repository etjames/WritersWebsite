from django.contrib import admin

# Register your models here.
from .models import Submission, WritingType, Genre, Theme
admin.site.register(Submission)
admin.site.register(WritingType)
admin.site.register(Genre)
admin.site.register(Theme)