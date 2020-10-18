from django.contrib import admin
from .models import Lecture, Discussion_or_Lab
# Register your models here.
admin.site.register(Lecture)
admin.site.register(Discussion_or_Lab)