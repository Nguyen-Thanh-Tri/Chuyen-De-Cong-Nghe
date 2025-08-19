from django.db.models import F
from querysets.models import Blog, Entry

Entry.objects.filter(number_of_comments__gt=F("number_of_pingbacks"))

Entry.objects.filter(number_of_comments__gt=F("number_of_pingbacks") * 2)

Entry.objects.filter(rating__lt=F("number_of_comments") + F("number_of_pingbacks"))

Entry.objects.filter(authors__name=F("blog__name"))

from datetime import timedelta
Entry.objects.filter(mod_date__gt=F("pub_date") + timedelta(days=3))

F("somefield").bitand(16)

#Expressions can reference transforms

Entry.objects.filter(pub_date__year=F("mod_date__year"))
from django.db.models import Min
Entry.objects.aggregate(first_published_year=Min("pub_date__year"))

from django.db.models import OuterRef, Subquery, Sum
Entry.objects.values("pub_date__year").annotate(
    top_rating=Subquery(
        Entry.objects.filter(
            pub_date__year=OuterRef("pub_date__year"),
        )
        .order_by("-rating")
        .values("rating")[:1]
    ),
    total_comments=Sum("number_of_comments"),
)


#The pk lookup shortcut


# Blog.objects.get(id__exact=14)  
# Blog.objects.get(id=14) 
# Blog.objects.get(pk=14)

# # Get blogs entries with id 1, 4 and 7
# Blog.objects.filter(pk__in=[1, 4, 7])

# # Get all blog entries with id > 14
# Blog.objects.filter(pk__gt=14)

# Entry.objects.filter(blog__id__exact=3)  # Explicit form
# Entry.objects.filter(blog__id=3)  # __exact is implied
# Entry.objects.filter(blog__pk=3)  # __pk implies __id__exact


#Caching and QuerySets
print("Caching and QuerySets------------------------------")
print([e.headline for e in Entry.objects.all()])
print([e.pub_date for e in Entry.objects.all()])

queryset = Entry.objects.all()
print([p.headline for p in queryset])  
print([p.pub_date for p in queryset])

#When QuerySets are not cached

print("When QuerySets are not cached-----------------------")
queryset = Entry.objects.all()
print(queryset[5])  # Queries the database
print(queryset[5])  # Queries the database again

queryset = Entry.objects.all()
[entry for entry in queryset]  # Queries the database
print(queryset[5])  # Uses cache
print(queryset[5])  # Uses cache

# [entry for entry in queryset]
# bool(queryset)
# entry in queryset
# list(queryset)