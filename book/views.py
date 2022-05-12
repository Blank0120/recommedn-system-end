import json

from django.http import HttpResponse
from rest_framework import generics
from book.serializers import *

# Create your views here.
class bookList(generics.ListAPIView):
    queryset = book.objects.all().order_by('?')[0:20]
    serializer_class = bookSerializer

class userList(generics.ListAPIView):
    queryset = user.objects.all()[0:20]
    serializer_class = userSerializer

    def userLogin(HttpRequest):
        print(HttpRequest.body)
        body_unicode = HttpRequest.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        userID = body_data['userID']
        password = body_data['password']

        u = user.objects.filter(UserID=userID,password=password)
        print(str(u.values()[0]))
        return HttpResponse(str(u.values()[0]))

class bookRatingsList(generics.ListAPIView):
    queryset = bookRatings.objects.all()[0:20]
    serializer_class = bookRatingsSerializer




