from modellayer.models import Place, Restaurant

Place.objects.all().delete()
Restaurant.objects.all().delete()

p1 = Place.objects.create(name="Bob's Cafe", address="123 Main St")
p2 = Place.objects.create(name="Central Perk", address="90 Bedford St")
p3 = Place.objects.create(name="The Coffee House", address="42 Wallaby Way")

r1 = Restaurant.objects.create(
    name="Pizza Palace", address="456 Elm St", serves_hot_dogs=False, serves_pizza=True
)
r2 = Restaurant.objects.create(
    name="Hotdog Heaven", address="789 Oak St", serves_hot_dogs=True, serves_pizza=False
)
r3 = Restaurant.objects.create(
    name="Bob's Cafe", address="123 Main St", serves_hot_dogs=True, serves_pizza=True
)

Place.objects.filter(name="Bob's Cafe")
print("hehehehehe")
Restaurant.objects.filter(name="Bob's Cafe")