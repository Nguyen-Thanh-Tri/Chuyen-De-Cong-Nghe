from modellayer.models import Person1, MyPerson


p = Person1.objects.create(first_name="foobar")
MyPerson.objects.get(first_name="foobar")