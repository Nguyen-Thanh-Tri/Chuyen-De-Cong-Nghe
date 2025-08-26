from django.shortcuts import render
from django.http import HttpResponse

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
