from django.shortcuts import render
from .models import Score
from django.views.generic.edit import CreateView, DeleteView

def index(request):
    scores = Score.objects.all()
    return render(request, 'index.html', {'scores': scores})

class ScoreCreate(CreateView):
    model = Score
    fields = '__all__'
    success_url = '/'

class ScoreDelete(DeleteView):
    model = Score
    success_url = '/'
