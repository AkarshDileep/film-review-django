from django.db import models

# Create your models here.
class review(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'live'),(DELETE,'delete'))
    name=models.IntegerField()
    reviews=models.TextField()
    mail=models.EmailField()
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)

    