from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('snippets/', views.snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', views.snippet_detail, name='snippet-detail'),
]

# Cho phép URL như .json, .api tùy theo format suffix nếu muốn
urlpatterns = format_suffix_patterns(urlpatterns)
