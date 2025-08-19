from querysets.models import Blog, Entry

from datetime import date
beatles = Blog.objects.create(name="Beatles Blog")
pop = Blog.objects.create(name="Pop Music Blog")
Entry.objects.create(
    blog=beatles,
    headline="New Lennon Biography",
    pub_date=date(2008, 6, 1),
)

Entry.objects.create(
    blog=beatles,
    headline="New Lennon Biography in Paperback",
    pub_date=date(2009, 6, 1),
)

Entry.objects.create(
    blog=pop,
    headline="Best Albums of 2008",
    pub_date=date(2008, 12, 15),
)

Entry.objects.create(
    blog=pop,
    headline="Lennon Would Have Loved Hip Hop",
    pub_date=date(2020, 4, 1),
)

Blog.objects.filter(
    entry__headline__contains="Lennon",
    entry__pub_date__year=2008,
)

Blog.objects.filter(
    entry__headline__contains="Lennon",
).filter(
    entry__pub_date__year=2008,
)

