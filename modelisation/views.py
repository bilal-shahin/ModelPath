from django.shortcuts import render
from django.http import FileResponse,HttpResponse
from django.core.files.images import ImageFile
from discngine.settings import STATICFILES_DIRS
import os
from .functions import search, search_metabolites, search_reactions
from .forms import SearchMetabolitesForm, SearchReactionsForm
from modelisation.models import Metabolites, Reactions, GSModels

# Create your views here.

def index(request):
    return render(request, 'index.html')


def models(request):
    output = {'model':GSModels.objects.get(id='iML1515')}
    return render(request, 'see_model.html', context=output)

def reactions(request):
    output = search(request, SearchReactionsForm, search_reactions, 'reactions')
    return render(request,'search_reactions.html',context=output)

def metabolites(request):
    output = search(request, SearchMetabolitesForm, search_metabolites, 'metabolites')
    return render(request,'search_metabolites.html',context=output)

def genes(request):
    return HttpResponse("""
         <h1>Bienvenue sur mon site !</h1>
         <p>Ici ce sera les <strong>genes</strong> !</p>
         """)

def escher(request):
    return HttpResponse("""
         <h1>Bienvenue sur mon site !</h1>
         <p>Ici ce sera l'api <strong>escher</strong> !</p>
         """)

def see_metabolite(request, metabolite_id):
    output = {'metabolite':Metabolites.objects.get(pk=metabolite_id)}
    return render(request,'see_metabolite.html',context=output)

def get_image(request, metabolite_id):
    imagefile = ImageFile(open(os.path.join(STATICFILES_DIRS[0],'images','2D_molecule',metabolite_id+'.png'), 'rb'))
    return HttpResponse(imagefile, content_type = 'image/png')

def see_reaction(request, reaction_id):
    output = {'reaction': Reactions.objects.get(pk=reaction_id)}
    return render(request, 'see_reaction.html', context=output)