from modellayer.models import Person
p = Person(name="Fred Flintstone", shirt_size="L")
p.save()
p.shirt_size
p.get_shirt_size_display()