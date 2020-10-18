from django.db import models
from django.urls import reverse

# Create your models here.
class Lecture(models.Model):
    index = models.IntegerField(primary_key=True)
    department = models.CharField(max_length=4)
    course_num = models.IntegerField()
    course_name = models.CharField(max_length=100)
    class_num = models.IntegerField()
    section_num = models.IntegerField()
    class_type = models.CharField(max_length=7) #Change to 10 for discussions and labs
    credits = models.IntegerField()
    seat_count = models.IntegerField()
    filled_seats = models.IntegerField(default=0)
    meeting_place = models.CharField(max_length=35)
    professor = models.CharField(max_length=30)
    start_time = models.CharField(max_length=4)
    end_time = models.CharField(max_length=4)
    date_nums = models.CharField(max_length=15)
    discussion_lab_nums = models.CharField(max_length=250)

    def meeting_days(self):
        output = ""
        for date in self.date_nums.split(', '):
            if date == 'TBA':
                output = 'TBA'
            elif date == '1':
                output += 'Mo'
            elif date == '2':
                output += 'Tu'
            elif date == '3':
                output += 'We'
            elif date == '4':
                output += 'Th'
            elif date == '5':
                output += 'Fr'
            elif date == '6':
                output += 'Sa'
        return output

    def meeting_times(self):
        start_time = self.start_time
        end_time = self.end_time
        meeting_time = ''
        if start_time == 'TBA':
            meeting_time = 'TBA'
        elif end_time == 'TBA':
            meeting_time = 'TBA'
        else:
            start_time = int(self.start_time)
            end_time = int(self.end_time)
            if start_time > 1300:
                start_time -= 1200
                start_time = str(start_time)
                start_time = "" + start_time[:len(start_time) - 2] + ":" + start_time[len(start_time) - 2:] + "pm"
            else:
                start_time = str(start_time)
                start_time = "" + start_time[:len(start_time) - 2] + ":" + start_time[len(start_time) - 2:] + "am"
            if end_time > 1300:
                end_time -= 1200
                end_time = str(end_time)
                end_time = "" + end_time[:len(end_time) - 2] + ":" + end_time[len(end_time) - 2:] + "pm"
            else:
                end_time = str(end_time)
                end_time = "" + end_time[:len(end_time) - 2] + ":" + end_time[len(end_time) - 2:] + "am"
            meeting_time = start_time + "-" + end_time
        return meeting_time

    def __str__(self):
        return(str(self.index))

    def get_absolute_url(self):
        return reverse('lecture', kwargs={'pk': self.index})

class Discussion_or_Lab(models.Model):
    index = models.IntegerField(primary_key=True)
    department = models.CharField(max_length=4)
    course_num = models.IntegerField()
    course_name = models.CharField(max_length=100)
    class_num = models.IntegerField()
    section_num = models.IntegerField()
    class_type = models.CharField(max_length=10) #Change to 10 for discussions and labs
    credits = models.IntegerField()
    seat_count = models.IntegerField()
    filled_seats = models.IntegerField(default=0)
    meeting_place = models.CharField(max_length=35)
    professor = models.CharField(max_length=30)
    start_time = models.CharField(max_length=4)
    end_time = models.CharField(max_length=4)
    date_nums = models.CharField(max_length=10)
    lecture_num = models.IntegerField()

    def meeting_days(self):
        output = ""
        for date in self.date_nums.split(', '):
            if date == 'TBA':
                output = 'TBA'
            elif date == '1':
                output += 'Mo'
            elif date == '2':
                output += 'Tu'
            elif date == '3':
                output += 'We'
            elif date == '4':
                output += 'Th'
            elif date == '5':
                output += 'Fr'
            elif date == '6':
                output += 'Sa'
        return output

    def meeting_times(self):
        start_time = self.start_time
        end_time = self.end_time
        meeting_time = ''
        if start_time == 'TBA':
            meeting_time = 'TBA'
        elif end_time == 'TBA':
            meeting_time = 'TBA'
        else:
            start_time = int(self.start_time)
            end_time = int(self.end_time)
            if start_time > 1300:
                start_time -= 1200
                start_time = str(start_time)
                start_time = "" + start_time[:len(start_time) - 2] + ":" + start_time[len(start_time) - 2:] + "pm"
            else:
                start_time = str(start_time)
                start_time = "" + start_time[:len(start_time) - 2] + ":" + start_time[len(start_time) - 2:] + "am"
            if end_time > 1300:
                end_time -= 1200
                end_time = str(end_time)
                end_time = "" + end_time[:len(end_time) - 2] + ":" + end_time[len(end_time) - 2:] + "pm"
            else:
                end_time = str(end_time)
                end_time = "" + end_time[:len(end_time) - 2] + ":" + end_time[len(end_time) - 2:] + "am"
            meeting_time = start_time + "-" + end_time
        return meeting_time

    def __str__(self):
        return (str(self.class_num))

    def get_absolute_url(self):
        return reverse('d_l', kwargs={'pk': self.index})

