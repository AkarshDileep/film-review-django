from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class userr(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'live'),(DELETE,'delete'))
    name=models.CharField(max_length=200)
    email=models.EmailField()
    dob=models.DateField(default=10/4/2024)
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name='customer_profile')
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)

    def __str__(self) -> str:
        return self.name