from django.db import models


class Score(models.Model):
    player = models.IntegerField(null=False)
    computer = models.IntegerField(null=False)
    name = models.CharField(max_length=25)
    timestamp = models.DateTimeField(auto_now_add=True)

    
