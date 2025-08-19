from querysets.models import Blog, ThemeBlog, Entry

#Copying model instances

print("\nCopying model instances\n")

blog = Blog(name="My blog", tagline="Blogging is easy")
blog.save()  # blog.pk == 1

blog.pk = None
blog._state.adding = True
blog.save()  # blog.pk == 2

django_blog = ThemeBlog(name="Django", tagline="Django is easy", theme="python")
django_blog.save()  # django_blog.pk == 3

django_blog.pk = None
django_blog.id = None
django_blog._state.adding = True
django_blog.save()  # django_blog.pk == 4

entry = Entry.objects.all()[0]  # some previous entry
old_authors = entry.authors.all()
entry.pk = None
entry._state.adding = True
entry.save()
entry.authors.set(old_authors)


#Updating multiple objects at once
print("\nUpdating multiple objects at once\n")

Entry.objects.filter(pub_date__year=2007).update(headline="Everything is the same")
b = Blog.objects.get(pk=1)
Entry.objects.update(blog=b)

b = Blog.objects.get(pk=1)
Entry.objects.filter(blog=b).update(headline="Everything is the same")

