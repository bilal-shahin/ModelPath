from modelisation.models import GSModels, Reactions, Metabolites, Genes, Reaction_model, Reaction_products, Reaction_substrates
from django.db.models import Q, F, Count
import re



def search(request, form_class, search_func, data):
    """wrap the POST request to process and call the search_objects function on data

    Args:
        request (request object): request object
        form_class (class): Form class to call
        data (str): data string element

    Returns:
        [dict]: context dictionnary output with data
    """
    output = {}
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            target = form.cleaned_data
            output[data] = search_func(target, data)
    else:
        form =  form_class()
    output['search_form'] = form
    return output


def search_metabolites(target, data=None):
    """Returns QuerySet with objects containining target in their relevant fields.

    Args:
        target (dict): dictionnary of metabolites form POST values

    Returns:
        [QuerySet]: QuerySet with the desired data
    """
    targets = [x for x in target['search_field'].split() if len(x)>0]
    res = Metabolites.objects.none()
    for metabolite in targets:
        res |= Metabolites.objects.filter(
            Q(id__icontains=metabolite) |
            Q(name__icontains=metabolite) |
            Q(formula__icontains=metabolite) |
            Q(inchikey__icontains=metabolite) 
        )
    return res

def search_reactions(target, data=None):
    res = Reactions.objects.all()
    # search by ID
    if target['reactions_id']:
        id_query = Reactions.objects.none()
        targets = [x for x in target['reactions_id'].split()]
        for reaction in targets:    
            id_query |= Reactions.objects.filter(
                Q(id__icontains=reaction) |
                Q(name__icontains=reaction)
            )
        res = res.intersection(id_query)

    if target['reactions_models']:
        models_query = Reactions.objects.none()
        targets = [x for x in target['reactions_models'].split()]
        for model in targets:
            models_query |= Reactions.objects.filter(models__id__icontains=model)
        res = res.intersection(models_query)

    if target['reactions_substrates']:
        substrates_query = Reactions.objects.none()
        targets = [x for x in target['reactions_substrates'].split()]
        for substrate in targets:
            substrates_query |= Reactions.objects.filter(substrates__id__icontains=substrate)
        res = res.intersection(substrates_query)

    if target['reactions_products']:
        products_query = Reactions.objects.none()
        targets = [x for x in target['reactions_products'].split()]
        for product in targets:
            products_query |= Reactions.objects.filter(products__id__icontains=product)
        res = res.intersection(products_query)

    if target['reactions_ec_number']:
        ec_query = Reactions.objects.none()
        targets = [x for x in target['reactions_ec_number'].split()]
        for code in targets:
            ec_query |= Reactions.objects.filter(ec_number__contains=code)
        res = res.intersection(ec_query)

    return res.order_by('id')
