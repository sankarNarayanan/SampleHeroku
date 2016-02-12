from django.db import models


class userTable(models.Model):
    userName = models.CharField(max_length=200,primary_key=True)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    emailId = models.CharField(max_length=200)


