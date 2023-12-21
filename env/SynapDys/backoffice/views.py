from django.shortcuts import render, get_object_or_404
from .models import Lesson, Progress
from .forms import ProgressForm

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, template_name='lesson_detail.html', context= {'lesson': lesson})



def track_progress(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    user_progress, created = Progress.objects.get_or_create(user=request.user.userprofile, lesson=lesson)

    if request.method == 'POST':
        form = ProgressForm(request.POST, instance=user_progress)
        if form.is_valid():
            form.save()
    else:
        form = ProgressForm(instance=user_progress)

    return render(request, template_name='track_progress.html', context={'form': form})

def template(request):
    return render(request, template_name='template.html')

def lecon_CM2_Fr_Adjectif(request):
    return render(request, template_name='CM2_Fr_Lecon_Adjectif.html')

def lecon_CM2_Fr_Adjectif_eval(request):
    return render(request, template_name='CM2_Fr_Lecon_Adjectif_eval.html')