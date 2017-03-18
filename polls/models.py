import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone



# Create your models here.
@python_2_unicode_compatible # only if you need to support Python 2
class Question(models.Model):
    """Polls Question"""
    # def __init__(self, arg):
    #     super(Question, self).__init__()
    #     self.arg = arg
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published.')

    def __str__(self):
        return self.question_text

    def published_recently(self):
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        # return self.pub_date <= now

    published_recently.admin_order_field = 'pub_date'
    published_recently.boolean = True
    published_recently.short_description = 'Published recently?'


@python_2_unicode_compatible # only if you need to support Python 2
class Choice(models.Model):
    """Polls Question Choices"""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
