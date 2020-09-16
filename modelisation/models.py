from django.db import models
import wikipedia

# Create your models here.
class Metabolites(models.Model):
    id            = models.CharField(max_length=100, primary_key=True, unique=True)
    name          = models.CharField(max_length=255, null=True, blank=True)
    summary       = models.TextField(default='') 
    formula       = models.CharField(max_length=255, null=True, blank=True)
    smiles        = models.TextField(null=True, blank=True)
    inchikey      = models.CharField(max_length=27, null=True, blank=True)
    compartment   = models.CharField(max_length=50, null=True, blank=True)
    charge        = models.IntegerField(null=True, blank=True)
    mol_weight    = models.FloatField(null=True, blank=True)
    mnxm          = models.CharField(max_length=30, null=True, blank=True)
    chebi         = models.CharField(max_length=30, null=True, blank=True)
    bigg          = models.CharField(max_length=30, null=True, blank=True)
    biocyc        = models.CharField(max_length=30, null=True, blank=True)
    kegg_compound = models.CharField(max_length=30, null=True, blank=True)
    kegg_drug     = models.CharField(max_length=30, null=True, blank=True)
    hmdb          = models.CharField(max_length=30, null=True, blank=True)
    sabiork       = models.CharField(max_length=30, null=True, blank=True)
    sbo           = models.CharField(max_length=30, null=True, blank=True)
    seed          = models.CharField(max_length=30, null=True, blank=True)
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name if self.name else self.id

    def get_summary(self):
        try:
            summary = wikipedia.summary(self.name, sentences=3)
        except:
            summary = ''
        return summary

    def save(self, *args, **kwargs):
        if self.name:
            self.summary = self.get_summary()
        super(Metabolites, self).save(*args, **kwargs)


class Reactions(models.Model):
    id         = models.CharField(max_length=30, primary_key=True, unique=True)
    name       = models.CharField(max_length=255, null=True, blank=True)
    subsystem  = models.CharField(max_length=255, null=True, blank=True)
    ec_number  = models.TextField(null=True, blank=True)
    mnxr       = models.CharField(max_length=50, null=True, blank=True)
    seed       = models.CharField(max_length=50, null=True, blank=True)
    bigg       = models.CharField(max_length=50, null=True, blank=True)
    biocyc     = models.CharField(max_length=50, null=True, blank=True)
    kegg       = models.CharField(max_length=50, null=True, blank=True)
    rhea       = models.CharField(max_length=50, null=True, blank=True)
    sbo        = models.CharField(max_length=50, null=True, blank=True)
    substrates = models.ManyToManyField(Metabolites,through='Reaction_substrates',related_name='substrates')
    products   = models.ManyToManyField(Metabolites,through='Reaction_products',related_name='products')
    models     = models.ManyToManyField('GSModels', through='Reaction_model',related_name='models')
    
    
    def __str__(self):
        return self.name if self.name else self.id

    def get_metabolites_stochiometry(self):
        output = {}
        for substrate in self.substrates.all():
            output[substrate] = self.reaction_substrates_set.get(substrate_id=substrate.id).stochiometry
        for product in self.products.all():
            output[product] = self.reaction_products_set.get(product_id=product.id).stochiometry
        return output


class Genes(models.Model):
    id       = models.CharField(max_length=30, primary_key=True, unique=True)
    name     = models.CharField(max_length=30, null=True, blank=True)
    synonyms = models.TextField(null=True, blank=True)
    bigg     = models.CharField(max_length=50, null=True, blank=True)
    asap     = models.CharField(max_length=50, null=True, blank=True)
    ncbi     = models.CharField(max_length=50, null=True, blank=True)
    uniprot  = models.CharField(max_length=50, null=True, blank=True)
    sbo      = models.CharField(max_length=50, null=True, blank=True)
    reaction = models.ManyToManyField(Reactions,blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name if self.name else self.id


class GSModels(models.Model):
    id          = models.CharField(max_length=30, primary_key=True, unique=True)
    organism    = models.CharField(max_length=255)
    metabolites = models.ManyToManyField(Metabolites)
    reactions   = models.ManyToManyField(Reactions, through='Reaction_model', related_name='reactions')
    genes       = models.ManyToManyField(Genes)
    objective   = models.TextField(null=True)
    nb_metabolites = models.IntegerField(null=True, blank=True)
    nb_reactions = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.id


class Reaction_substrates(models.Model):
    reaction     = models.ForeignKey(Reactions, on_delete=models.CASCADE, null=True)
    substrate    = models.ForeignKey(Metabolites, on_delete=models.CASCADE, null=True, blank=True)
    stochiometry = models.IntegerField()

    class Meta:
        unique_together = ('reaction', 'substrate')


class Reaction_products(models.Model):
    reaction     = models.ForeignKey(Reactions, on_delete=models.CASCADE, null=True)
    product      = models.ForeignKey(Metabolites, on_delete=models.CASCADE, null=True, blank=True)
    stochiometry = models.IntegerField()

    class Meta:
        unique_together = ('reaction', 'product')


class Reaction_model(models.Model):
    reaction    = models.ForeignKey(Reactions, on_delete=models.CASCADE)
    model       = models.ForeignKey(GSModels, on_delete=models.CASCADE)
    lower_bound = models.FloatField(default=0.0)
    upper_bound = models.FloatField(default=1000.0)

    class Meta:
        unique_together = ('reaction', 'model')


