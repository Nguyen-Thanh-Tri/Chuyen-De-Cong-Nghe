from polls.models import Question
from django.utils import timezone

Question.objects.all()

q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
q.id
q.question_text
q.pub_date
q.question_text = "What's up?"
q.save()
Question.objects.all()