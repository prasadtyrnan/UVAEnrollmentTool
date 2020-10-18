from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wish_list = models.TextField(max_length=255, default="")
    year = models.IntegerField(default=1)
    major_1 = models.CharField(max_length=255, default="Undecided")
    major_2 = models.CharField(max_length=255, default="NONE")
    semester_1 = models.TextField(max_length=1000, default="")
    semester_2 = models.TextField(max_length=1000, default="")
    semester_3 = models.TextField(max_length=1000, default="")
    semester_4 = models.TextField(max_length=1000, default="")
    semester_5 = models.TextField(max_length=1000, default="")
    semester_6 = models.TextField(max_length=1000, default="")
    semester_7 = models.TextField(max_length=1000, default="")
    semester_8 = models.TextField(max_length=1000, default="")

    def get_wish_list_indices(self):
        output = []
        for course in self.wish_list.split(','):
            output.append(course)
        return output
