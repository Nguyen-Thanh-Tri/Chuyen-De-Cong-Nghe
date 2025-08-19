from modellayer.models import Person, Group, Membership
from datetime import date

ringo = Person.objects.create(name="Ringo Starr")
john = Person.objects.create(name="John Lennon")
george = Person.objects.create(name="George Harrison")
paul = Person.objects.create(name="Paul McCartney")
beatles = Group.objects.create(name="The Beatles")
m1 = Membership(
    person=ringo,
    group=beatles,
    date_joined=date(1962, 8, 16),
    invite_reason="Needed a new drummer.",
)
m1.save()
beatles.members.all()
ringo.group_set.all()
m2 = Membership.objects.create(
    person=paul,
    group=beatles,
    date_joined=date(1960, 8, 1),
    invite_reason="Wanted to form a band.",
)
beatles.members.all()


Membership.objects.get_or_create(
    person=ringo,
    group=beatles,
    defaults={
        "date_joined": date(1968, 9, 4),
        "invite_reason": "You've been gone for a month and we miss you."
    }
)
beatles.members.all()
beatles.members.remove(ringo)
beatles.members.all()
beatles.members.clear()
Membership.objects.all()

Group.objects.filter(members__name__startswith="Paul")


Person.objects.filter(
    group__name="The Beatles", membership__date_joined__gt=date(1961, 1, 1)
)


ringos_membership = Membership.objects.get(group=beatles, person=ringo)
ringos_membership.date_joined
ringos_membership.invite_reason
ringos_membership = ringo.membership_set.get(group=beatles)
ringos_membership.date_joined
ringos_membership.invite_reason