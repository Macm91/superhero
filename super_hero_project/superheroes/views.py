from superhero_project.super_hero_project import superheroes
from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from .models import Superhero



# Create your views here.
def index(request): 
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes' : all_heroes
    }
    return render(request,'superheroes/index.html', context)

def detail (request, hero_id):
    hero = Superhero.objects.get(pk = hero_id)
    context = {
        'hero' : hero
    }
    return render(request, 'superheroes/details.html', context)

def create (request):
    if request.method== "POST":
       name=request.POST.get ('name')
       alter_ego=request.POST.get('alter_ego')
       primary_ability = request.POST.get('primary_ability')
       secondary_ability = request.POST.get('secondary_ability')
       catch_phrase = request.POST.get('catch_phrase')
       new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary_ability, secondary_abilty= secondary_ability, catch_phrase=catch_phrase)
       new_hero.save()
       return HttpResponseRedirect(reverse ('superheroes:index'))
    else:    
        return render(request, 'superheroes/create.html')

    
def edit(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    if request.method=='POST':
        single_hero.name = request.POST.get('name')
        single_hero.alter_ego = request.POST.get('alter_ego')
        single_hero.primary_ability = request.POST.get('primary_ability')
        single_hero.secondary_ability = request.POST.get('secondary_ability')
        single_hero.catch_phrase = request.POST.get('catch_phrase')
        single_hero.save()
        return HttpResponseRedirect (reverse( 'superheroes:index'))
    else:    
        context={
            'single_hero': single_hero
        }
        return render (request, "superheroes/edit.html", context)
  

def delete(request, hero_id):
    context={}
    single_hero = Superhero.objects.get(pk=hero_id)
    single_hero.delete()
    return HttpResponseRedirect(reverse('superheroes:index'))