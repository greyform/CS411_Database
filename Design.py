
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):  # __unicode__ on Python 2
        return self.first_name


class Sample(models.Model):

    Accession = models.CharField(max_length=30, primary_key=True)
    Topology = models.CharField(max_length=30, null=True)
    MolecularType = models.CharField(max_length=30, null=True)
    DataClass = models.CharField(max_length=30, null=True)
    SequenceLength = models.INTEGER
    Sequence = models.TextField
    SequenceVersion = models.CharField(max_length=30, null=True)
    DateAdded = models.DateField
    TaxonomicDivision = models.CharField(max_length=30, null=True)


class Publication(models.Model):
    DOI = models.IntegerField(primary_key=True)
    Author = models.CharField(max_length=30)
    Journal = models.CharField(max_length=30)
    PublicationDate = models.DateField
    URL = models.URLField


class Organism(models.Model):
    Species = models.CharField(max_length=30,  primary_key=True)
    Genus = models.CharField(max_length=30, primary_key=True)
    Family = models.CharField(max_length=30)
    Order = models.CharField(max_length=30)
    Class = models.CharField(max_length=30)
    Phylum = models.CharField(max_length=30)
    Kingdom = (
        ('AR', 'Archaebacteria'),
        ('EU', 'Eubacteria'),
        ('PR', 'Protista'),
        ('FU', 'Fungi'),
        ('PL','Plantae'),
        ('AN', 'Animalia')
    )


class Reference(models.Model):
    Accession = models.ForeignKey(Samples, on_delete=models.CASCADE)
    DOI = models.ForeignKey(Publications, on_delete=models.CASCADE)


class From (models.Model):
    Accession = models.ForeignKey(Samples, on_delete=models.CASCADE)
    Species = models.ForeignKey(Organisms, on_delete=models.CASCADE)
    Genus = models.ForeignKey(Organisms, on_delete=models.CASCADE)


p = Publication.objects.create(DOI='filler', Author='Chris Pratt', Journal='Nature', PublicationDate="Jan.4, 2011", URL="https://en.wikipedia.org/")
s = Sample(Accession='111', SequenceLength=5,  Sequence='sldkfjlksdjf', DateAdded ="Jan.4, 2011")
r = Reference(Accession='111', DOI = 'filler')








