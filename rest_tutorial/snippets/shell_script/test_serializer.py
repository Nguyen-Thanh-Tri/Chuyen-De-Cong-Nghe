# test_serializer.py
import sys
import django
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Cấu hình Django settings để dùng model
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
django.setup()

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# Tạo object mẫu
snippet = Snippet(code='print("hello, world")')
snippet.save()

# Serialize object vừa tạo
serializer = SnippetSerializer(snippet)
print("Kết quả serialize 1 object:")
print(serializer.data)

# Serialize nhiều object (QuerySet)
snippets = Snippet.objects.all()
serializer = SnippetSerializer(snippets, many=True)
print("\nKết quả serialize nhiều object:")
print(serializer.data)
