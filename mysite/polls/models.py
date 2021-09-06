import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # DISABLED below because it shows future post as recently publisehed
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now() # new logic labels the cutting line is yesterday <= the Question date <= now 
        return now - datetime.timedelta(days=1) <= self.pub_date <= now  

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text