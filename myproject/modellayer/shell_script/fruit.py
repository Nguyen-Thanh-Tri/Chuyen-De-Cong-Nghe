from modellayer import Fruit
fruit = Fruit.objects.create(name="Apple")
fruit.name = "Pear"
fruit.save()
Fruit.objects.values_list("name", flat=True)