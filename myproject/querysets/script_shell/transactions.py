from querysets.models import Dog
from django.db.models import Value, JSONField


#Storing and querying for None
print("\nStoring and querying for None\n")

Dog.objects.create(name="Max", data=None)  # SQL NULL.
Dog.objects.create(name="Archie", data=Value(None, JSONField()))  # JSON null.
Dog.objects.filter(data=None)
Dog.objects.filter(data=Value(None, JSONField()))
Dog.objects.filter(data__isnull=True)
Dog.objects.filter(data__isnull=False)


#Key, index, and path transforms
print("\nKey, index, and path transforms\n")

Dog.objects.create(
    name="Rufus",
    data={
        "breed": "labrador",
        "owner": {
            "name": "Bob",
            "other_pets": [
                {
                    "name": "Fishy",
                }
            ],
        },
    },
)
Dog.objects.create(name="Meg", data={"breed": "collie", "owner": None})
Dog.objects.filter(data__breed="collie")
Dog.objects.filter(data__owner__name="Bob")
Dog.objects.filter(data__owner__other_pets__0__name="Fishy")

Dog.objects.create(name="Shep", data={"breed": "collie"})
Dog.objects.filter(data__owner__isnull=True)



#Complex lookups with Q objects
print("\nComplex lookups with Q objects\n")
from django.db.models import Q
Q(question__startswith="What")
Q(question__startswith="Who") | Q(question__startswith="What")
Q(question__startswith="Who") | ~Q(pub_date__year=2005)

