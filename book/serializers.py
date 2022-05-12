from rest_framework import serializers
from book.models import *

class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = ['ISBN','BookTitle','BookAuthor','YearOfPublication','Publisher','ImageURLS','ImageURLM','ImageURLL']

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['UserID','Location','Age']

class bookRatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookRatings
        fields = ['UserID','ISBN','BookRating']