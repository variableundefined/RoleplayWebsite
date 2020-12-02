from django.shortcuts import render, get_object_or_404
from .models import spell, school, tag
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'list/index.html')

def spell_detail(request, pk):
    gotspell = get_object_or_404(spell, pk=pk)
    return render(request, 'list/spell_detail.html', {'spell': gotspell})

def spell_list(request):
    schools = school.objects.all()
    spells = spell.objects.all()
    tags = tag.objects.all()
    return render(request, 'list/spell_list.html', {'schools': schools, 'spells': spells, 'tags': tags})

def table_list(request):
    spells = spell.objects.all()
    return render(request, 'list/table_list.html', {'spells': spells})