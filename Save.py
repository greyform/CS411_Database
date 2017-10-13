from Design import Publication
import Design


p = Publication.objects.create(DOI='filler', Author='Chris Pratt', Journal='Nature', PublicationDate="Jan.4, 2011", URL="https://en.wikipedia.org/")
s = Sample(Accession='111', SequenceLength=5,  Sequence='sldkfjlksdjf', DateAdded ="Jan.4, 2011")
r = Model.Reference(Accession='111', DOI = 'filler')

p.save()
s.save()
r.save()

f = Design.Person.objects

Manager.raw(raw_query, params=None, translations=None)¶
ref = Model.Reference.object.get(Accession='111', DOI='filler')
ref = Model.Reference.object.get(Accession='111', DOI='filler')
