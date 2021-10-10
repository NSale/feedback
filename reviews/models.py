from django.db import models


# Create your models here.
class Feedback(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField(max_length=200)
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.user_name} has written \'{self.review_text}\' and gave it a rating of {self.rating}.'
