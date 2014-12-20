from django.shortcuts import render, redirect
from django import forms
from coaches.models import Coach


class CoachModelForm(forms.ModelForm):
    class Meta:
        model = Coach


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

def coach_edit(request, coach_id=None):
    if coach_id is None:
        coach = Coach()
    else:
        coach = Coach.objects.get(id=coach_id)
    if request.method == 'POST':
        form = CoachModelForm(request.POST,  instance=coach)
        if form.is_valid():
            coach.save()
            return redirect('coaches:list')
    else:
        form = CoachModelForm(instance=coach)
    return render(request, 'coaches/edit.html', {'form': form})

def coach_remove(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    coach.delete()
    return redirect('coaches:list')
