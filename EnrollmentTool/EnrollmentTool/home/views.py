from django.shortcuts import render, get_object_or_404, redirect
from .models import Lecture, Discussion_or_Lab
from django.views.generic import ListView
# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def search(request):
    if request.GET.get('search'):
        course_num = str(request.GET.get('course-num'))
        department = str(request.GET.get('department'))
        if course_num == '':
            course_num = 'NONE'
        if department == '':
            print('no department')
            department = 'NONE'
        if course_num == 'NONE' and department == 'NONE':
            return redirect('search')
        return redirect('/search_results/lv/' + department + '/' + course_num)
    return render(request, 'home/search.html')

class SearchListView(ListView):
    model = Lecture
    template_name = 'home/search_results.html'
    paginate_by = 12
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SearchListView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['department'] = self.kwargs.get('dp')
        context['course_num'] = self.kwargs.get('cn')
        return context
    def get_queryset(self):
        if self.kwargs.get('dp') == 'NONE':
            return Lecture.objects.filter(course_num=self.kwargs.get('cn'))
        elif self.kwargs.get('cn') == 'NONE':
            return Lecture.objects.filter(department=self.kwargs.get('dp'))
        return Lecture.objects.filter(department=self.kwargs.get('dp'), course_num=self.kwargs.get('cn'))

def lecture_detail_view(request, pk):
    lecture = get_object_or_404(Lecture, index=pk)
    discussions = []
    for discussion in lecture.discussion_lab_nums.split(', '):
        if(discussion == 'None'):
            break
        discussions.append(Discussion_or_Lab.objects.get(pk=discussion))
    has_discussions = len(discussions) > 0
    return render(request, 'home/lecture_detail.html', context={'object':lecture, 'has_discussions':has_discussions, 'discussions':discussions})

def discussion_detail_view(request, pk):
    discussion = get_object_or_404(Discussion_or_Lab, index=pk)
    meeting_days = ""
    for date in discussion.date_nums.split(', '):
        if date == 'TBA':
            meeting_days = 'TBA'
        elif date == '1':
            meeting_days += 'Mo'
        elif date == '2':
            meeting_days += 'Tu'
        elif date == '3':
            meeting_days += 'We'
        elif date == '4':
            meeting_days += 'Th'
        elif date == '5':
            meeting_days += 'Fr'
        elif date == '6':
            meeting_days += 'Sa'
    start_time = discussion.start_time
    end_time = discussion.end_time
    meeting_time = ''
    if start_time == 'TBA':
        meeting_time = 'TBA'
    elif end_time == 'TBA':
        meeting_time = 'TBA'
    else:
        start_time = int(discussion.start_time)
        end_time = int(discussion.end_time)
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
    return render(request, 'home/discussion_detail.html', context={'object':discussion, 'm_d':meeting_days, 'meeting_time':meeting_time})

