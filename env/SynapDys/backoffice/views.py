import json,os,base64
from django.shortcuts import render, get_object_or_404
from .models import Lesson, Progress
from .forms import ProgressForm, TexteForm
from gtts import gTTS
from django.http import HttpResponse, JsonResponse
import os


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

def lecon_CM2_Fr_Lecon_Adjectif(request):
    return render(request, 'lecon_CM2_Fr_Lecon_Adjectif.html')

def lecon_CM2_Fr_Lecon_Adjectif_eval(request):
    # Logique de la vue
    return render(request, 'lecon_CM2_Fr_Lecon_Adjectif_eval.html')

def synthese_vocale(request):
    if request.method == 'POST':
        texte = request.POST.get('texte', '')

        # Utilisation de gTTS pour générer la synthèse vocale
        tts = gTTS(text=texte, lang='fr')
        audio_data = tts.get_audio_data()

        # Convertir les données audio en base64 pour la lecture directe dans le navigateur
        audio_base64 = base64.b64encode(audio_data).decode('utf-8')

        return JsonResponse({'audio_base64': audio_base64})
    else:
        # Le cas GET retourne simplement le template
        return render(request, 'synthese_vocale.html')

def template(request):
    return render(request, template_name='template.html')
