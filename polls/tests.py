import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here.
class QuestionMethodsTest(TestCase):
    def test_published_recently_with_future_question(self):
        """
        published_recently() should return False for Question
        whose pub_date is in future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.published_recently(), False)

def test_published_recently_with_old_question(self):
    """
    published_recently() should return False for Question
    whose pub_date is older than 1 day.
    """
    time = timezone.now() + datetime.timedelta(days=30)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.published_recently(), False)

def test_published_recently_with_recent_question(self):
    """
    published_recently() should return False for Question
    whose pub_date within the last day.
    """
    time = timezone.now() + datetime.timedelta(hours=1)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.published_recently(), True)
