from django.db import models

# Create your models here.
class movie(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'live'),(DELETE,'delete'))
    title=models.CharField(max_length=200)
    rating=models.IntegerField()
    review=models.TextField()
    description=models.TextField()
    image=models.ImageField(upload_to='media/')
    actor=models.ImageField()
    actress=models.ImageField()
    priority=models.IntegerField()
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)

    def __str__(self) -> str:
        return self.title