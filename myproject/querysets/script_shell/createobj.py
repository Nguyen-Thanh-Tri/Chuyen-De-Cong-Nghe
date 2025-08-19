from querysets.models import Blog, Entry, Author
from datetime import date

b = Blog(name="Beatles Blog", tagline="All the latest Beatles news.")
b.save()



cheese_blog = Blog(name="Cheddar Talk")
cheese_blog.save()


entry = Entry.objects.create(
    blog=cheese_blog,
    headline="Cheese is great",
    body_text="Cheese blog entry body text here...",
    pub_date=date.today(), 
    number_of_comments=0,
    number_of_pingbacks=0,
    rating=5
)

entry = Entry.objects.get(pk=1)
cheese_blog = Blog.objects.get(name="Cheddar Talk")
entry.blog = cheese_blog
entry.save()

joe = Author.objects.create(name="Joe")
entry.authors.add(joe)

john = Author.objects.create(name="John")
paul = Author.objects.create(name="Paul")
george = Author.objects.create(name="George")
ringo = Author.objects.create(name="Ringo")
entry.authors.add(john, paul, george, ringo)


Blog.objects
b = Blog(name="Foo", tagline="Bar")
b.objects

all_entries = Entry.objects.all()

q1 = Entry.objects.filter(headline__startswith="What")
q2 = q1.exclude(pub_date__gte=date.today())
q3 = q1.filter(pub_date__gte=date.today())


q = Entry.objects.filter(headline__startswith="What")
q = q.filter(pub_date__lte=date.today())
q = q.exclude(body_text__icontains="food")
print(q)

#Retrieving a single object with get()
one_entry = Entry.objects.get(pk=1)

#điều này trả về 5 đối tượng đầu tiên
Entry.objects.all()[:5]
#Điều này trả về đối tượng thứ sáu đến thứ mười
Entry.objects.all()[5:10]
#trả về danh sách tất cả các đối tượng thứ hai trong số 10 đối tượng đầu tiên
Entry.objects.all()[:10:2]


#trả về đối tượng đầu tiên trong cơ sở dữ liệu, sau khi sắp xếp các mục theo thứ tự bảng chữ cái theo tiêu đề
Entry.objects.order_by("headline")[0]
#tương đương với
Entry.objects.order_by("headline")[0:1].get()

