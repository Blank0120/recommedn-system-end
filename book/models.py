from django.db import models

# Create your models here.

class book(models.Model):
    ISBN = models.CharField(primary_key=True,max_length=13,null = False,default='')
    BookTitle = models.CharField(max_length=255,null=True,blank=True)
    BookAuthor = models.CharField(max_length=255,null=True,blank=True)
    YearOfPublication = models.IntegerField(null=True,blank=True)
    Publisher = models.CharField(max_length=255,null=True,blank=True)
    ImageURLS = models.CharField(max_length=255,null=True,blank=True)
    ImageURLM = models.CharField(max_length=255,null=True,blank=True)
    ImageURLL = models.CharField(max_length=255,null=True,blank=True)
    rate = models.IntegerField(default=0)


class user(models.Model):
    UserID = models.IntegerField(primary_key=True,null=False,default=10)
    password = models.CharField(max_length=255,null=False,default=123)
    Location = models.CharField(max_length=255,null=True,blank=True)
    Age = models.IntegerField(null=True,blank=True)

class bookRatings(models.Model):
    ID = models.AutoField(primary_key=True)

    UserID = models.IntegerField(default=0,null=False)
    ISBN = models.CharField(max_length=13,null=False,default='')
    BookRating = models.IntegerField(null=False,default=0)

    class Meta:
        unique_together = ('UserID','ISBN')