from django.contrib import admin
from django.urls import path
from modelisation import views

urlpatterns = [
    path('models/', views.models, name='models'),
    path('reactions/', views.reactions, name='reactions'),
    path('see_reaction/<str:reaction_id>', views.see_reaction, name='see_reaction'),
    path('metabolites/', views.metabolites, name='metabolites'),
    path('see_metabolite/<str:metabolite_id>', views.see_metabolite,name='see_metabolite'),
    path('get_image/<str:metabolite_id>',views.get_image,name='get_image'),
    path('genes/', views.genes, name='genes'),
    path('escher/', views.escher, name='escher'),
]