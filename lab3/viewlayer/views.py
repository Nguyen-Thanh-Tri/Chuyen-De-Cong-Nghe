from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

#CONFURL
# Create your views here.
def home(request):
    return HttpResponse("Xin chào! Đây là trang Home của app viewlayer.")

def about(request):
    return HttpResponse("Trang About của viewlayer.")

#URL động (có tham số)
def year_archive(request, year):
    return HttpResponse(f"Archive năm {year}")

def month_archive(request, year, month):
    return HttpResponse(f"Archive tháng {month}/{year}")

#converters vs slug
def article_detail(request, year, slug):
    return HttpResponse(f"Xem bài viết: {slug}, năm {year}")

#-----------------------------------------------------------------------------------------------------------------------
#VIEWFUNC
import datetime

#basic
def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html lang="en"><body>It is now %s.</body></html>' % now
    return HttpResponse(html)

#response error
def my_view(request):
    if request.GET.get("x") == "1":
        return HttpResponse("<h1>OK</h1>")
    else:
        return HttpResponseNotFound("<h1>Page not found</h1>")
    
#http404
from django.http import Http404

def detail(request, item_id):
    if item_id != 1:   
        raise Http404("Item does not exist")
    return HttpResponse("Item exists")

#custom error views
def my_custom_404(request, exception):
    return render(request, "404.html", {}, status=404)

def my_custom_500(request):
    return render(request, "500.html", {}, status=500)

#---------------------------------------------------------------------
#CLASS_BASE VIEW
from django.views import View

class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World")
    
#templatview
from django.views.generic import TemplateView, ListView

class AboutView(TemplateView):
    template_name = "about.html"

#listview
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = "book_list.html"   
    context_object_name = "books"

import asyncio
class AsyncHelloView(View):
    async def get(self, request):
        await asyncio.sleep(1)  
        return HttpResponse("Hello async world!")