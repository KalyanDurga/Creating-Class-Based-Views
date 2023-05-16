from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=50,primary_key=True)

    def __str__(self) -> str:
        return self.topic_name
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    url=models.URLField()
    email=models.EmailField()

    def __str__(self) -> str:
        return self.name