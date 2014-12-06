from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def coaches_list(request):
    coaches = Coach.objects.all()
    return render(request, 'coaches/list.html', {'coaches': coaches})

def coach_item(request, coach_id):
    coach = Coach.objects.get(id=int(coach_id))
    try:
        course = Course.objects.get(teacher=int(coach_id))
    except:
        course = None
    return render(request, 'coaches/item.html', {'coach': coach,
                                                 'course': course})
