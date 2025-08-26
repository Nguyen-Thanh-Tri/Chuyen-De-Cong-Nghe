from django.db import models
from django.views import View
from django.http import HttpResponse

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()

class ContactView(View):
    def get(self, request):
        return HttpResponse("Form liên hệ")

    def post(self, request):
        name = request.POST.get("name")
        return HttpResponse(f"Xin chào {name}")